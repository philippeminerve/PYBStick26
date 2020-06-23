import ili9341 # Import de la bibliothèque ili9341
import ustruct # Module de conversions des valeurs Python en structures C 
from time import * # Nécessaire pour mesurer les temps d'affichage
from machine import Pin, SPI # Bibliothèque de gestion des entrées sorties

# Initialise la liaison SPI à une fréquence de 24Mhz avec 3 pins matériels dédiés PybStick26
spi = SPI(baudrate=24000000,miso=Pin("S21"), mosi=Pin("S19", Pin.OUT), sck=Pin("S23", Pin.OUT))
# Objet display basé sur la classe ILI9341 et initialisé avec le SPI et les deux derniers pins de notre montage
display = ili9341.ILI9341(spi, cs=Pin("S11"), dc=Pin("S5"), rst=Pin("S3"))		

# On définit la taille de la zone : ici la totalité de l'écran
width = 240
height = 320

t0 = ticks_ms()
display._write(0x2a, ustruct.pack(">HH", 0, width-1))
display._write(0x2b, ustruct.pack(">HH", 0, height-1))
display._write(0x2c)
display._data(b'\x00\x00'*(50*width+60))
display._data(b'\x00\x1f'*(51*width-(width-60)))
print(ticks_ms()-t0, "ms pour afficher 50 + 1/4 lignes noires et 50 + 3/4 lignes bleues")


