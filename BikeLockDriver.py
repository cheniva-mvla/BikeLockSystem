#--------------MAIN DRIVER FUNCTIONALITY------------#
#-----Libraries
import sys
#sys.path.insert(1, '\git\BikeLockSystem\Classes')
#sys.path.insert(2, '\git\BikeLockSystem\Misc')

from Classes import BikeLockGPIO 
from Classes import BikeLockCamera 
from Misc import CheckStatus
from threading import Thread
from time import sleep

#----- Variable Setup
BLGPIO = BikeLockGPIO.BLGPIO #BikeLock GPIO 
BLCamera = BikeLockCamera.BLCamera #BikeLock Camera
BLSafteyCheckup = CheckStatus #Checks overall board functionality 

pins = {
    "Output": 25, #Alarm
    "Output": 17, #LED
    "Output": 16, #Shackle 1 Output
    "Output": 20, #Shackle 2 Output
    "Input": 19, #Shackle 1 Input
    "Input": 26, #Shackle 2 Input

    }

#------ Instantiate Classes
BLGPIO.__init__(BLGPIO, pins)

#------ Status Check
safetyCheck = False  
if safetyCheck: 
    Thread(target = BLSafteyCheckup.checkPins, args = (10,)).start()
    Thread(target = BLSafteyCheckup.record10SecondVideo).start()

#================ Logic =================#



#------ Functions
def printInfo():
    #- safeLock check. True = On; False = Off
    print("GPIO safeLock: " + str(not BLGPIO.getSafeLock(BLGPIO)))
    print("Camera safeLock: " + str(not BLCamera.getSafeLock(BLGPIO)))
    print() #whitespace

    #- print out information
    print(BLGPIO.__str__(BLGPIO))
    print(BLGPIO.getPins(BLGPIO))
    print() #whitespace

    print(BLCamera.__str__(BLGPIO))

def trigger(): 
    Thread(target = BLGPIO.blink, args = (BLGPIO, 25, 10,)).start()
    Thread(target = BLCamera.RecordTenSecondVideo, args = (BLCamera,)).start() 

def standby(inputPin, OutputPin):
    return not BLGPIO.detectCircut(BLGPIO, inputPin, OutputPin)

#--------main loop----------
alert = False
detect = False
reset = False
standByTime = 1
#printInfo()
print("Shackle wire one circut completed:" + str(standby(19, 16)))
print("Shackle wire two circut completed:" + str(standby(26, 20)))

while(False):
    if detect: #trigger mode
        trigger()
        detect = False
        alert = True
    elif not alert: #standby mode
        detect = standby(25) #if standby is false, no alarm should be raised and the circut is completed. True if circut is broken. 

    if reset:
        alert = False
        detect = False

    sleep(standByTime)
    




