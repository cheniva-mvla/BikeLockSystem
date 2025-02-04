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
    "Alarm": 25,
    "LED": 17,
    "Shackle": 30, #change later, currently random pin
    }

#------ Instantiate Classes
BLGPIO.__init__(BLGPIO, pins)

#------ Status Check
safetyCheck = False  
if safetyCheck: 
    Thread(target = BLSafteyCheckup.checkPins, args = (10,)).start()
    Thread(target = BLSafteyCheckup.record10SecondVideo).start()

#================ Logic =================#
#- safeLock check. True = On; False = Off
print("GPIO safeLock: " + str(not BLGPIO.getSafeLock(BLGPIO)))
print("Camera safeLock: " + str(not BLCamera.getSafeLock(BLGPIO)))
print() #whitespace

#- print out information
print(BLGPIO.__str__(BLGPIO))
print(BLGPIO.getPins(BLGPIO))
print() #whitespace

print(BLCamera.__str__(BLGPIO))

#------ Functions
    
def trigger(): 
    Thread(target = BLGPIO.blink, args = (BLGPIO, 25, 10,)).start()
    Thread(target = BLCamera.RecordTenSecondVideo, args = (BLCamera,)).start() 

def standby():
    return not BLGPIO.detectCircut()

#--------main loop----------
Alert = False
detect = False
reset = False
standByTime = 1
while(True):
    if detect: #trigger mode
        trigger()
        detect = False
        Alert = True
    elif not Alert: #standby mode
        detect = standby() #if standby is false, no alarm should be raised and the circut is completed. True if circut is broken. 

    if reset:
        Alert = False
        detect = False

    sleep(standByTime)
    




