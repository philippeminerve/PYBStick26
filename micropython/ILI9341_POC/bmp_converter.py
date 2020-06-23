#!/usr/bin/env python
# coding: utf8
"""
BMP conversion up to 240x320 resolution from 24bits to 16bits without padding
Use for high speed stream for ILI9341
"""

import sys
current_platform = sys.platform

if current_platform in ['linux','win32','darwin']:
    import struct
else:
    #For micropython 'esp32' and 'pyboard'
    import ustruct as struct

#####################################################
#Define filename and directory as \directory\filename

directory = 'Pictures'

#Change image name !!!

name = 'imageV'

#####################################################
filename = directory+'/'+name+'.bmp'

BMP_file = open(filename, 'rb')
C_BMP_file = open(directory+'/'+name+'16'+'.bmp', "wb")

try:
    """
    Reading header file to collect date and create adapted header for the converted file to keep it readable (except reverse color)
    """
    BMP_file.read(18)
    data = BMP_file.read(4)
    width = struct.unpack('<HH', data)[0]
    if width not in (240,320): print('Alert : 320 or 240 for full screen, file value width :', width)
    data = BMP_file.read(4)
    height = struct.unpack('<HH', data)[0]
    if height not in (240,320): print('Alert : 320 or 240 for full screen, file value height :', height)
    BMP_file.read(2)
    data = BMP_file.read(2)
    colorBits = struct.unpack('<H', data)[0]
    if colorBits != 24: raise ValueError('Error : Inappropriate Number of bytes by pixel - normal 24 versus ' + str(colorBits))
    BMP_file.read(24)
    # Padding calculate for 32 bits row BMP specification
    padding = width*3%4
    
    #Pixel conversion
    nbpixel = 0
    for row in range(height): # For each row
        pixelBuffer = bytearray() #Create a buffer to store pixel
        for pixel in range(width): # For each pixel in one row
            unpacked_data = struct.unpack('BBB', BMP_file.read(3)) #Read RGB value of pixel
            r = unpacked_data[2]
            g = unpacked_data[1]
            b = unpacked_data[0]
            pixelto16 = struct.pack('>H',(r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3)
            pixelBuffer.append(pixelto16[0])
            pixelBuffer.append(pixelto16[1])
            nbpixel = nbpixel+1
        C_BMP_file.write(pixelBuffer)
        if padding > 0 : BMP_file.read(padding)
    print(row, ' rows completed.',nbpixel,'pixels generated')
finally:
    BMP_file.close()
    C_BMP_file.close()
