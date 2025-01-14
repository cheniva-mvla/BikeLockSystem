import RPi.GPIO as GPIO         
from time import sleep       
import picamera   

pin = 25                     

GPIO.setmode(GPIO.BCM)         
GPIO.setwarnings(False)        
GPIO.setup(pin, GPIO.OUT)   

def TurnPowerOnAndOff(bool):
    if bool: 
        GPIO.output(pin, GPIO.HIGH)  
        print("Powering Pin " + str(pin))      
    else:
        GPIO.output(pin, GPIO.LOW)    
        print("Unpowering Pin " + str(pin))    

def PowerPin25():
    while True:                         
        TurnPowerOnAndOff(True)
        sleep(1)     
        TurnPowerOnAndOff(False)
        sleep(1)

with picamera.Picamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()

    sleep(2)

    camera.capture('BikeLockImage.jpg')
