#--------------RFID FUNCTIONALITY------------#
safeLock = True 
if safeLock:
    import RPi.GPIO as GPIO   
    from mfrc522 import SimpleMFRC522
    from time import sleep   
else:
    pass


rfid = SimpleMFRC522()

while True:
    id, text = rfid.read()
    print(id)
    print(text)