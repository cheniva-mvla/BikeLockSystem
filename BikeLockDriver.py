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

#----- Constants 
#Shackles
shackleOneOutput = 23
shackleOneInput = 27
shackleTwoOutput = 24
shackleTwoInput = 22 

#Physical Outouts
AlarmOutput = 25
LEDOutput = 17

#Misc
RFIDKey = None #change later 
AccelerometorInput = None #change later 

#FSM Vars
alert = False
detect = False
reset = False
standByTime = 2


pins = {
    AlarmOutput: "Output", #Alarm
    LEDOutput: "Output", #LED

    shackleOneOutput: "Output", #Shackle 1 Output
    shackleTwoOutput: "Output", #Shackle 2 Output

    shackleOneInput: "Input", #Shackle 1 Input
    shackleTwoInput: "Input", #Shackle 2 Input
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
    print("Pin Information: ")
    print(BLGPIO.getPins(BLGPIO))
    print() #whitespace

    print(BLCamera.__str__(BLGPIO))

def reportPinConnectivity():
    print("Shackle wire one circut completed:" + str(standby(shackleOneInput, shackleOneOutput)))
    print("Shackle wire two circut completed:" + str(standby(shackleTwoInput, shackleTwoOutput)))

def trigger(): 
    Thread(target = BLGPIO.blink, args = (BLGPIO, LEDOutput, 10,)).start()
    #Thread(target = BLCamera.RecordTenSecondVideo, args = (BLCamera,)).start() 

def standby(inputPin, OutputPin):
    return BLGPIO.detectCircut(BLGPIO, inputPin, OutputPin)

def checkDetection():
    if not standby(shackleOneInput, shackleOneOutput):
        return True
    if not standby(shackleTwoInput, shackleTwoOutput):
        return True
    return False 
    
#--------main loop----------
#printInfo()
reportPinConnectivity()
#trigger()
while(True):
    if detect: #trigger mode
        print("Alarm Triggered")
        trigger()
        alert = True
        detect = False
    elif not alert: #standby mode
        print("Standby")
        detect = checkDetection() #if standby is false, no alarm should be raised and the circut is completed. True if circut is broken. 
        print("Detect Status: " + str(detect))
    if reset:
        alert = False
        detect = False
    reportPinConnectivity()


    sleep(standByTime)
    




