""" Programme de test pour neopixel sur Matrice 8x8
Nécessite l'usage de la bibliothèque ws2812 : https://github.com/mchobby/esp8266-upy/blob/master/neopixel/lib/ws2812.py
NB: Carte SD nécessaire en raison de la taille bibliothèque + code

Le code pour la gestion des images est inspiré du fonctionnement SenseHat via des listes Pythons formatées.
NB: En l'état la conversion d'image se fait sur matrice carrée avec inversion de sens des leds entre deux lignes.

Le pin S19/SPI (4eme pin en bas à droite USB vers le haut) est utilisé
PHM le 17/04/2020
"""
from ws2812 import NeoPixel

from time import sleep
nbled = 64

# Choix d'une intensité à 0.5 pour limiter la consommation à 1A
np = NeoPixel( spi_bus=1, led_count=nbled, intensity=0.5 )

#On définit les couleurs utilisées
O=(0,0,0) # LED eteinte
B=(0,0,255) # Bleu
J=(255,255,0) # Jaune
R=(255,105, 180) # Rose

#On créé des dessins à partir des couleurs existantes
logo = [
    O, O, O, B, B, B, O, O,
    O, O, B, B, B, J, B, O,
    O, O, B, B, B, B, B, O,
    O, O, B, B, B, B, J, J,
    B, B, B, B, B, B, B, O,
    O, B, B, B, B, B, B, O,
    O, O, O, B, B, B, O, O,
    O, O, J, O, O, J, O, O,
    ]

coeur = [
    O, O, O, O, O, O, O, O,
    O, R, R, O, O, R, R, O,
    R, O, O, R, R, O, O, R,
    R, O, O, O, O, O, O, R,
    O, R, O, O, O, O, R, O,
    O, O, R, O, O, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

coeur2 = [
    O, O, O, O, O, O, O, O,
    O, R, R, O, O, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
  
def afficherImage(image): 
  """ fonction qui inverse une ligne sur 2 """
  for uneLed in range(nbled):
    if (uneLed//nbled**0.5)%2 : #Avec un Not on créé une symétrie verticale
    #  Colonnes paires
    	np[uneLed] = image[uneLed]
    else :
    #  Colonnes impaires = inversion de l'ordre des leds
		np[uneLed] = image[int(((1+uneLed//nbled**0.5)*(nbled**0.5)-1)-(uneLed%nbled**0.5))]
  np.write()
  print("l\'image est affichée")
  
def wheel(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    r = g = b = 0
  elif pos < 85:
    r = int(pos * 3)
    g = int(255 - pos * 3)
    b = 0
  elif pos < 170:
    pos -= 85
    r = int(255 - pos * 3)
    g = 0
    b = int(pos * 3)
  else:
    pos -= 170
    r = 0
    g = int(pos * 3)
    b = int(255 - pos * 3)
  return (r, g, b)


def rainbow_cycle(wait):
  for j in range(255):
    for i in range(nbled):
      pixel_index = (i * 256 // nbled) + j
      np[i] = wheel(pixel_index & 255)
    np.write()
    sleep(wait)

# Appels de test


#Affichage de l'image de profil philippeminerve
afficherImage(logo)
sleep( 2 )
#Affichage d'un raimbow cycle
rainbow_cycle(0.0005)
sleep( 0.5 )
#Affichage de l'image coeur évidé
afficherImage(coeur)
sleep(2)

#Affichage de l'animation coeur évidé coeur plein
durbattement = 0.1
nbbattement = 8

for i in range(nbbattement):
	afficherImage(coeur2)
	sleep(durbattement)
	afficherImage(coeur)
	sleep(durbattement)

afficherImage(coeur2)
sleep(2)

# On éteint tout
np.fill( (0,0,0) )
np.write()	
