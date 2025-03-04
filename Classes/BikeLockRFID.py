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

def readRFID():
    while True:
        id, text = rfid.read()
        print(id)
        print(text)
        if id == bikeLockFobID or id == bikeLockCardID: 
            print("Acess Granted")
            return 
      

readRFID()