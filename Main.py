from gpiozero import Buzzer
from time import sleep 

buzzer = Buzzer(17)

print("Pi is on")

while True:
    Buzzer.beep()

