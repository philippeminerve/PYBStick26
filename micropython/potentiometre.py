"""
Programme variation de led avec potentiometre
Branchement de la LED (pate +) entre la borne S7 (4ème broche en partant du haut à gauche - USB vers le haut)
et la masse (pate -) borne (1ère broche en bas à gauche - USB vers le haut)

Le potentiometre se branche entre le 3,3V (1ère broche en haut à gauche - USB vers le haut)
la masse (5ème broche en partant du haut à gauche - USB vers le haut)
L'entrée analogique S23 (2eme broche en bas à gauche - USB vers le haut)

"""

from machine import Pin
from pyb import ADC, Timer
import time

# On initialise la sortie 7 pour piloter la led
maLED = Pin( "S7", Pin.OUT )

# On ajoute de quoi gérer la fonctionnalité PWM (timer 4 et channel 1)sur la sortie 7
monTimer = Timer(4, freq=1000)
maSortiePWM = monTimer.channel(1, Timer.PWM, pin=maLED)

# On initialise l'entree analogique sur l'entrée 23
potentiometre = ADC(Pin("S23"))
valPotentiometre = 0

#-- map(valeur, fromLow, fromHigh, toLow, toHigh) --> renommée rescale
def rescale(valeur, in_min, in_max, out_min, out_max):
    return (valeur - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    # d'après la fonction map du fichier wirin.c du core Arduino


while True: #Equivalent de la boucle loop en arduino
    
    # On mesure la valeur du potentiometre entre 0 et 4095
    valPotentiometre = potentiometre.read()
    pourcentage = rescale(valPotentiometre,0,4095,0,100)
    maSortiePWM.pulse_width_percent(pourcentage)
