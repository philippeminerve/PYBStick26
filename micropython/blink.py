"""
Programme Blink d'une LED
Branchement de la LED (pate +) entre la borne S7 (4ème broche en partant du haut à gauche - USB vers le haut)
et la masse (pate -) borne (1ère broche en bas à gauche - USB vers le haut)
"""

from machine import Pin
import time

# On initialise la sortie 7 pour piloter la led
maLED = Pin( "S7", Pin.OUT )


while True: #Equivalent de la boucle loop en arduino
	print("je commence mon blink") # On affiche dans Putty le texte Je commence mon blink
	maLED.high() #La broche S7 au niveau haut - la led est allumée
	time.sleep_ms(500) #Attendre 500 ms
	maLED.low() #La broche S7 au niveau bas - la led est éteinte
	time.sleep_ms(500) #Attendre 500 ms
