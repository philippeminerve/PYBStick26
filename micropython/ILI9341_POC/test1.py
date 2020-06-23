import ili9341 # Import de la bibliothèque ili9341
from time import * # Nécessaire pour mesurer les temps d'affichage
from machine import Pin, SPI # Bibliothèque de gestion des entrées sorties

# Initialise la liaison SPI à une fréquence de 24Mhz avec 3 pins matériels dédiés PybStick26
spi = SPI(baudrate=24000000,miso=Pin("S21"), mosi=Pin("S19", Pin.OUT), sck=Pin("S23", Pin.OUT))
# Objet display basé sur la classe ILI9341 et initialisé avec le SPI et les deux derniers pins de notre montage
display = ili9341.ILI9341(spi, cs=Pin("S11"), dc=Pin("S5"), rst=Pin("S3"))		

t0 = ticks_ms()
display.fill(ili9341.color565(0x00, 0x00, 0xff))
print(ticks_ms()-t0, "ms pour afficher une page bleue")
