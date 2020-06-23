import ili9341
import ustruct
from time import *
from machine import Pin, SPI

spi = SPI(baudrate=24000000,miso=Pin("S21"), mosi=Pin("S19", Pin.OUT), sck=Pin("S23", Pin.OUT))
display = ili9341.ILI9341(spi, cs=Pin("S11"), dc=Pin("S5"), rst=Pin("S3"))

# On définit la taille de la zone à traiter
width = 240
height = 320
width_sprite = 123
height_sprite = 114

# On modifie les réglages de l'écran pour faire miroir
display._write(0x36, b'\x08')

# On commence par remplir tout l'écran en blanc
display.fill(ili9341.color565(0xff, 0xff, 0xff))

t0 = ticks_ms()

display._write(0x2a, ustruct.pack(">HH", int((width-width_sprite)/2), int((width-width_sprite)/2)+width_sprite-1))
display._write(0x2b, ustruct.pack(">HH", int((height-height_sprite)/2), int((height-height_sprite)/2)+height_sprite-1))
display._write(0x2c)

cptImages = 0
dureeAnim = 10000

while (ticks_ms()-t0)<dureeAnim:
    for uneimage in range(11,25):
        filename = 'bird'+str(uneimage)+'.bmp'
        display._data(open(filename,'rb').read())
        cptImages = cptImages + 1
print(cptImages, "images diffusées durant", dureeAnim, "ms. Soit", 1000*cptImages/dureeAnim, "images/seconde")
# On termine avec un écran en blanc
display.fill(ili9341.color565(0xff, 0xff, 0xff))

