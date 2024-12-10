from gpiozero import Buzzer
from time import sleep 

buzzer = Buzzer(17)

print("Pi is on")

for i in range(10):
    Buzzer.beep()

