#--------------GPIO FUNCTIONALITY------------#

#-----Libraries
safeLock = True 
if safeLock:
    import RPi.GPIO as GPIO   
    from time import sleep   
else:
    pass

#-Class
class BLGPIO:

    #Note: Pins should have a dictionary setup
    '''
    It should have the format: "Function": GPIO Number
    i.e.
    Pins = {
    "Alarm": 25
    "LED": 17
    etc...
    }
    '''

 #----- Init 
    def __init__(self, pins):
        self.pins = pins
        if safeLock: 
            GPIO.setmode(GPIO.BCM)         
            GPIO.setwarnings(False)   
            for key, value in pins.items(): 
                if value == "Input":
                    GPIO.setup(key, GPIO.IN)
                else:
                    GPIO.setup(key, GPIO.OUT)
                    GPIO.output(key, GPIO.LOW)

#---- Getters and Setters
    def getPins(self):
        return self.pins 
    
    def getSafeLock(self):
        return safeLock
       
#---- Logic Functions
    def turnOn(pin):
        GPIO.output(pin, GPIO.HIGH)

    def turnOff(pin):
        GPIO.output(pin,GPIO.LOW)

    def toggle(pin):
        GPIO.output(pin, not GPIO.input(pin))

    def blink(self, pin, times):
        for i in times:
            self.toggle(pin)
            print("LED TOGGLED ON")
            sleep(1)
            self.toggle(pin)
            print("LED TOGGLED OFF")
            sleep(1)
    
    def detectCircut(self, inputPin, outputPin):
        GPIO.output(outputPin, GPIO.HIGH)
        state = GPIO.input(inputPin)
        return state #False if circut broken/D.N.E. True if circut completed. 
#---- Misc
    def __str__(self):
        return "I am GPIO"
                 


