#--------------GPIO FUNCTIONALITY------------#

#-----Libraries
#import RPi.GPIO as GPIO      

#-Class
class BLGPIO:
#----- Pin Setup

    #----- Init 
    def __init__(self, pins):
        '''
        GPIO.setmode(GPIO.BCM)         
        GPIO.setwarnings(False)       
        '''
        self.pins = pins
        # GPIO.setup(pins, GPIO.OUT, GPIO.LOW)

    
    def __str__(self):
        return "I am GPIO"

    def turnOn(pin):
        GPIO.output(pin, GPIO.HIGH)

    def turnOff(pin):
        GPIO.output(pin,GPIO.LOW)

    def toggle(pin):
        GPIO.output(pin, not GPIO.input(pin))
              


