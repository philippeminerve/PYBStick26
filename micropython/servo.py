"""
Programme Servo
Branchement du Servo
Fil rouge sur VIN (5V) (2ème broche en partant du haut à doite - USB vers le haut)
Fil noir sur masse (3ème broche en partant du haut à doite - USB vers le haut)
Fil orange sur Servo 1 (S12) (63ème broche en partant du haut à doite - USB vers le haut)

"""
from pyb import servo, delay

# On positionne le servo sur l'emplacement n°1 = S12
monServo = pyb.Servo(1)

while True: #Equivalent de la boucle loop en arduino
    
    for monAngle in range(-90,90,1):
        monServo.angle(monAngle)
        delay(15)
    for monAngle in range(90,-90,-1):
        monServo.angle(monAngle)
        delay(15)