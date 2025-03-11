#--------------RFID FUNCTIONALITY------------#
safeLock = True 
if safeLock:
    import RPi.GPIO as GPIO   
    from mfrc522 import SimpleMFRC522
    from time import sleep   
else:
    pass

rfid = SimpleMFRC522()
bikeLockFobID = 785924227828
bikeLockCardID = 703195382446

class BLRFID:
    LOCKED_STATE = False
    #----- Init     
    def __init__(self):
        pass 
    
    #----- RFID Functions
    def readRFID(self):
        while True: 
            print("Thread Running")
            id, text = rfid.read()
            if id == bikeLockFobID or id == bikeLockCardID: 
                print("Access Granted")
                self.LOCKED_STATE = True
            else:
                pass  
        
        #print(id)
        #print(text)

#----- Misc
    def __str__(self):
        return "RFID CLASS"
