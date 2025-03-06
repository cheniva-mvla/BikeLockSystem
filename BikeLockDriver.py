#--------------MAIN DRIVER FUNCTIONALITY------------#
#-----Libraries
import sys
#sys.path.insert(1, '\git\BikeLockSystem\Classes')
#sys.path.insert(2, '\git\BikeLockSystem\Misc')

from Classes import BikeLockGPIO 
from Classes import BikeLockCamera 
from Classes import BikeLockRFID

from Misc import CheckStatus
from threading import Thread
from time import sleep

#----- Variable Setup
BLGPIO = BikeLockGPIO.BLGPIO #BikeLock GPIO 
BLCamera = BikeLockCamera.BLCamera #BikeLock Camera
BLFRID = BikeLockRFID.BLRFID #Bike Lock RFID
BLSafteyCheckup = CheckStatus #Checks overall board functionality 

#----- Constants 
#Shackles with Board numbering
'''
Shackle One Output: GPIO 23 --> Board 16
Shackle One Input: GPIO 27 --> Board 13
Shackle Two Output: GPIO 24 --> Board 18
Shackle Two Input: GPIO 22 --> Board 15
'''
SHACKLE_ONE_OUTPUT = 16
SHACKLE_ONE_INPUT = 13
SHACKLE_TWO_OUTPUT = 18
SHACKLE_TWO_INPUT = 15 

#Physical Outouts
ALARM_OUTPUT = 10
LED_OUTPUT = 17 #in GPIO not in board

#Misc
RFID_KEY = None #change later 
AccelerometorInput = None #change later 

#FSM Vars
alert = False
detect = False
reset = False
standByTime = 2


pins = {
    ALARM_OUTPUT: "Output", #Alarm
    SHACKLE_ONE_OUTPUT: "Output",
    SHACKLE_ONE_INPUT: "Input",
    SHACKLE_TWO_OUTPUT: "Output",
    SHACKLE_TWO_INPUT: "Input"
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
    print() #whitespace
    print(BLFRID.__str__(BLFRID))


def reportPinConnectivity():
    print("Shackle wire one circut completed:" + str(standby(SHACKLE_ONE_INPUT, SHACKLE_ONE_OUTPUT)))
    print("Shackle wire two circut completed:" + str(standby(SHACKLE_TWO_INPUT, SHACKLE_TWO_OUTPUT)))

def trigger(): 
    Thread(target = BLGPIO.blink, args = (BLGPIO, ALARM_OUTPUT, 10,)).start()
    #Thread(target = BLCamera.RecordTenSecondVideo, args = (BLCamera,)).start() 

def standby(inputPin, OutputPin):
    return BLGPIO.detectCircut(BLGPIO, inputPin, OutputPin)

def checkDetection():
    if not standby(SHACKLE_ONE_INPUT, SHACKLE_ONE_OUTPUT):
        return True
    if not standby(SHACKLE_TWO_INPUT, SHACKLE_TWO_OUTPUT):
        return True
    return False 
    
#--------main loop----------

print("""
    #########################################
    ____  _   _ _   _ _   _ ___ _   _  ____ 
    |  _ \| | | | \ | | \ | |_ _| \ | |/ ___|
    | |_) | | | |  \| |  \| || ||  \| | |  _ 
    |  _ <| |_| | |\  | |\  || || |\  | |_| |
    |_| \_\\___/|_| \_|_| \_|___|_| \_|\____|        
    #########################################                           
""")

#printInfo()
#reportPinConnectivity()
#trigger()
BLFRID.readRFID(BLFRID)


while(False):
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
    




