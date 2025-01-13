import RPi.GPIO as GPIO         
from time import sleep          

pin = 25                     

GPIO.setmode(GPIO.BCM)         
GPIO.setwarnings(False)        
GPIO.setup(pin, GPIO.OUT)   

def turnOnPower():
    GPIO.output(pin, GPIO.HIGH)  
    print("Powering Pin " + str(pin))      

def turnOffPower():
    GPIO.output(pin, GPIO.LOW)    
    print("Unpowering Pin " + str(pin))      

while True:                         
    turnOnPower()
    sleep(1)     
    turnOffPower()
    sleep(1)