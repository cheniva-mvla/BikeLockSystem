#--------------MAIN DRIVER FUNCTIONALITY------------#
#-----Libraries
import sys, queue 
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
BLRFID = BikeLockRFID.BLRFID #Bike Lock RFID
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
LED_OUTPUT = 11     

#Misc
RFID_KEY = None #change later 
AccelerometorInput = None #change later 

#FSM Vars
alert = False
detect = False
reset = False
standByTime = 0.1


pins = {
    LED_OUTPUT: "Output",
    ALARM_OUTPUT: "Output", #Alarm
    SHACKLE_ONE_OUTPUT: "Output",
    SHACKLE_ONE_INPUT: "Input",
    SHACKLE_TWO_OUTPUT: "Output",
    SHACKLE_TWO_INPUT: "Input"
    }

#------ Instantiate Classes
BLGPIO.__init__(BLGPIO, pins)
BLCamera.__init__(BLCamera)

#------ Status Check (Debugging)
safetyCheck = False  
if safetyCheck: 
    Thread(target = BLSafteyCheckup.checkPins, args = (10,)).start()
    Thread(target = BLSafteyCheckup.record10SecondVideo).start()

#================ Logic =================#
#------ Functions
#Debugging
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
    print(BLRFID.__str__(BLRFID))

#Debugging
def reportPinConnectivity():
    print("Shackle wire one circut completed:" + str(detectShackleCircut(SHACKLE_ONE_INPUT, SHACKLE_ONE_OUTPUT)))
    print("Shackle wire two circut completed:" + str(detectShackleCircut(SHACKLE_TWO_INPUT, SHACKLE_TWO_OUTPUT)))

def trigger(): 
    Thread(target = BLGPIO.blink, args = (BLGPIO, LED_OUTPUT, 10,)).start()
    Thread(target = BLCamera.TakePicture, args = (BLCamera, )).start() 

def detectShackleCircut(inputPin, OutputPin):
    return BLGPIO.detectCircut(BLGPIO, inputPin, OutputPin)

def checkDetection():
    if not detectShackleCircut(SHACKLE_ONE_INPUT, SHACKLE_ONE_OUTPUT):
        return True
    if not detectShackleCircut(SHACKLE_TWO_INPUT, SHACKLE_TWO_OUTPUT):
        return True
    return False 
    
#--------main loop----------

print(
"""
#########################################
_____  _   _ _   _ _   _ ___ _   _  ____ 
|  _ \| | | | \ | | \ | |_ _| \ | |/ ___|
| |_) | | | |  \| |  \| || ||  \| | |  _ 
|  _ <| |_| | |\  | |\  || || |\  | |_| |
|_| \_\\___/|_| \_|_| \_|___|_| \_|\____|        
#########################################                           
""")

def BikeLockSystem():
    STANDBY = 0
    TRIGGER = 1
    UNLOCKED = 2

    TRIGGERED = False  

    DRIVER_STATE = 0
    
    unlockTimer = 0
    UNLOCK_TIME = 10 #lock can only be unlocked after 10 seconds. 
    UNLOCK_TIMER_BOUNDS = UNLOCK_TIME/standByTime 
    canUnlock = False

    Thread(target = BLRFID.readRFID, args = (BLRFID, )).start()

    while (True):
        if DRIVER_STATE == STANDBY:  

            print("STANDBY")
                
            if checkDetection(): 
                DRIVER_STATE = TRIGGER
            if not BLRFID.LOCKED_STATE and DRIVER_STATE != TRIGGER and canUnlock: 
                DRIVER_STATE = UNLOCKED 
                
                unlockTimer = 0
                canUnlock = False
        elif DRIVER_STATE == TRIGGER: 
            print("TRIGGER")

            if not TRIGGERED:
                TRIGGERED = True
                trigger()

            if not BLRFID.LOCKED_STATE:
                DRIVER_STATE = UNLOCKED 

        elif DRIVER_STATE == UNLOCKED: 
            print("UNLOCKED")

            if not checkDetection(): #Bike is locked 
                if BLRFID.LOCKED_STATE and canUnlock: 
                    DRIVER_STATE = STANDBY
                   
                    unlockTimer = 0
                    canUnlock = False
                    TRIGGERED = False 

                
        sleep(standByTime)
        unlockTimer += 1
        if unlockTimer >= UNLOCK_TIMER_BOUNDS: 
            canUnlock = True


'''
Address issue: if the tag is tapped twice during the 10 second interval, the read information saves and the bike will be unlocked after the time delay.
This may or  may not cause interference between states in the FSM. 

Current Tasks:
- Make Pi run single Application on boot
- Ensure that code is efficient. 
'''
#BLRFID.readRFID(BLRFID)
BikeLockSystem()
#printInfo()
#reportPinConnectivity()
#trigger()


