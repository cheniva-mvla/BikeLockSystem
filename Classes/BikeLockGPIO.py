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
        GPIO.setup(self.pin, GPIO.OUT)       
        '''
    def __str__(self):
        return "I am GPIO"
              


