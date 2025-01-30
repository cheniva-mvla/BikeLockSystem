#--------------BOARD CHECKUP FUNCTIONALITY------------#

#Libaries and Services
safeLock = True
if safeLock:
    import RPi.GPIO as GPIO         
    from time import sleep       
    from picamera2 import Picamera2, Preview
    from libcamera import Transform 
else:
    from time import sleep 
"""
#Checks if the physical board is working
    - check pin input/output
    - check camera
    - mostly not used, unless need to debug. 

**Currently using old main file logic
"""

def checkPins():
    pin = 25               

    GPIO.setmode(GPIO.BCM)         
    GPIO.setwarnings(False)        
    GPIO.setup(pin, GPIO.OUT)   

    for i in range(10):
        GPIO.output(pin, GPIO.HIGH)    
        print("LED TOGGLED ON")
        sleep(1)
        GPIO.output(pin, GPIO.LOW)    
        print("LED TOGGLED OFF")
        sleep(1)

def checkCamera():
    picam2 = Picamera2()
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    sleep(30)
    picam2.close() 


