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
#----------Camera Setup


#---------Functions
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

picam2 = Picamera2()
picam2.start_preview(Preview)

preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

picam2.start_and_record_video("TestBikeLockVideo.mp4", duration = 10, show_preview = True) #records a 10 second video
picam2.close()

#RecordTenSecondVideo()