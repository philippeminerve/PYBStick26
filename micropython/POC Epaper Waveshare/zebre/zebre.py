import epaper2in9 # Bibliothèque ecran
from machine import Pin, SPI # Bibliothèque de gestion des entrées sorties

# Init PybStick26
spi = SPI(baudrate=24000000,miso=Pin("S21"), mosi=Pin("S19", Pin.OUT), sck=Pin("S23", Pin.OUT))
cs=Pin("S11");dc=Pin("S5");rst=Pin("S3");busy = Pin("S8")

e = epaper2in9.EPD(spi, cs, dc, rst, busy)
e.init()

w = 128;h = 296;x = 0;y = 0

#on vide l'écran
e.clear_frame_memory(b'\xFF')
image = ('\x3e'*1184).encode()
e.set_frame_memory(image,x,y,w,h)

e.display_frame()
