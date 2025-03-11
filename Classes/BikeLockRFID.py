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
    LOCKED_STATE = True 
    #----- Init     
    def __init__(self):
        pass 
    
    #----- RFID Functions
    def readRFID(self):
        while True: 
            id, text = rfid.read()
            if id == bikeLockFobID or id == bikeLockCardID: 
                print("Access Granted")
                self.LOCKED_STATE = not self.LOCKED_STATE
            else:
                pass  
        
        #print(id)
        #print(text)

#----- Misc
    def __str__(self):
        return "RFID CLASS"
