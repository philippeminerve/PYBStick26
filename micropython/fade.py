"""
Programme fading d'une LED avec PWM
Branchement de la LED (pate +) entre la borne S7 (4ème broche en partant du haut à gauche - USB vers le haut)
et la masse (pate -) borne (1ère broche en bas à gauche - USB vers le haut)
"""

from machine import Pin
from pyb import Timer, delay
import time

# On initialise la sortie 7 pour piloter la led
maLED = Pin( "S7", Pin.OUT )

# On ajoute de quoi gérer la fonctionnalité PWM (timer 4 et channel 1)sur la sortie 7
monTimer = Timer(4, freq=1000)
maSortiePWM = monTimer.channel(1, Timer.PWM, pin=maLED)

maLuminosite = 0
monPasDeLuminosite = 5

while True: #Equivalent de la boucle loop en arduino
    
    # on indique un % de luminosité
    maSortiePWM.pulse_width_percent(maLuminosite)
    maLuminosite += monPasDeLuminosite
    
    if (maLuminosite<0 or maLuminosite>100):
        monPasDeLuminosite = -monPasDeLuminosite

    delay(30)
