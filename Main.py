#Libaries and Services
import RPi.GPIO as GPIO         
from time import sleep       
from picamera2 import Picamera2, Preview
from libcamera import Transform 


#--------------GPIO setup 
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

#----------Camera Setup
picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(30)
picam2.close()
