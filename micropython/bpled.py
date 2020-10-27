"""
Programme Bouton poussoir et d'une LED
Branchement de la LED (pate +) entre la borne S7 (4ème broche en partant du haut à gauche - USB vers le haut)
et la masse (pate -) borne (1ère broche en bas à gauche - USB vers le haut)
Le bouton poussoir entre la masse (5ème broche en partant du haut à gauche - USB vers le haut) et la borne S26 (1ère broche en bas à droite - USB vers le haut)
"""

from machine import Pin
import time

# On initialise la sortie 7 pour piloter la led
maLED = Pin( "S7", Pin.OUT )
monBouton = Pin( "S26", Pin.IN, Pin.PULL_UP)

# Par défaut bouton non pressé
etatBouton = 1;

while True: #Equivalent de la boucle loop en arduino
    etatBouton = monBouton.value()
    print("Etat du bouton {}".format(etatBouton))
    
    if (etatBouton == 0):
        maLED.high() #La broche S7 au niveau haut - la led est allumée
    else :
        maLED.low() #La broche S7 au niveau bas - la led est éteinte