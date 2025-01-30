#--------------MAIN DRIVER FUNCTIONALITY------------#
#-----Libraries
import sys
#sys.path.insert(1, '\git\BikeLockSystem\Classes')
#sys.path.insert(2, '\git\BikeLockSystem\Misc')

from Classes import BikeLockGPIO 
from Classes import BikeLockCamera 
from Misc import CheckStatus
from threading import Thread


#----- Variable Setup
BLGPIO = BikeLockGPIO.BLGPIO #BikeLock GPIO 
BLCamera = BikeLockCamera.BLCamera #BikeLock Camera
BLSafteyCheckup = CheckStatus #Checks overall board functionality 

pins = {
    "Alarm": 25,
    "LED": 17,
    }

#------ Instantiate Classes
BLGPIO.__init__(BLGPIO, pins)

#------ Status Check
safetyCheck = True 
if safetyCheck: 
    if __name__ == ' __main__':
        Thread(target=BLSafteyCheckup.checkPins).start()
        Thread(target=BLSafteyCheckup.record10SecondVideo).start()
    #BLSafteyCheckup.checkPins()
    #BLSafteyCheckup.checkCamera()
    #BLSafteyCheckup.record10SecondVideo()

#------ Logic
#- safeLock check. True = On; False = Off
print("GPIO safeLock: " + str(not BLGPIO.getSafeLock(BLGPIO)))
print("Camera safeLock: " + str(not BLCamera.getSafeLock(BLGPIO)))
print() #whitespace

#- print out information
print(BLGPIO.__str__(BLGPIO))
print(BLGPIO.getPins(BLGPIO))
print() #whitespace

print(BLCamera.__str__(BLGPIO))

