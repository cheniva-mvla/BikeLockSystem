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
standByTime = 0.01


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
    print(BLRFID.__str__(BLRFID))


def reportPinConnectivity():
    print("Shackle wire one circut completed:" + str(detectShackleCircut(SHACKLE_ONE_INPUT, SHACKLE_ONE_OUTPUT)))
    print("Shackle wire two circut completed:" + str(detectShackleCircut(SHACKLE_TWO_INPUT, SHACKLE_TWO_OUTPUT)))

def trigger(): 
    Thread(target = BLGPIO.blink, args = (BLGPIO, LED_OUTPUT, 10,)).start()
    #Thread(target = BLCamera.RecordTenSecondVideo, args = (BLCamera,)).start() 

def detectShackleCircut(inputPin, OutputPin):
    return BLGPIO.detectCircut(BLGPIO, inputPin, OutputPin)

def checkDetection():
    if not detectShackleCircut(SHACKLE_ONE_INPUT, SHACKLE_ONE_OUTPUT):
        return True
    if not detectShackleCircut(SHACKLE_TWO_INPUT, SHACKLE_TWO_OUTPUT):
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
#BLFRID.readRFID(BLFRID)
#trigger()

STANDBY = 0
TRIGGER = 1
UNLOCKED = 2
RFIDThread = Thread(target = BLRFID.readRFID, args = (BLRFID, self))

class BLDriver:
    #--Variables
    rfidResult = "fail"
    state = 0
    #--Constants 
 
    #----- Init 
    def __init__(self):
        pass

    def BikeLockSystem(self):
        while (True):
            RFIDThread.start()
            RFIDThread.join()
            print(self.rfidResult)

            if self.state == STANDBY:
                print("STANDBY")
                
                if checkDetection(): 
                    self.state = TRIGGER
                if BLRFID.readRFID(BLRFID) and self.state != TRIGGER: 
                    
                    self.state = UNLOCKED 
            elif self.state == TRIGGER: 

                print("TRIGGERED")

                if BLRFID.readRFID(BLRFID):
                    self.state = UNLOCKED 
            elif self.state == UNLOCKED: 

                print("UNLOCKED")

                if not checkDetection(): #Bike is locked 
                    if BLRFID.readRFID(BLRFID): 
                        self.state = STANDBY
                
            sleep(standByTime)

BLDriver.BikeLockSystem(BLDriver)

"""
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
    
"""



