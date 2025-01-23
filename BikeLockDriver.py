#--------------MAIN DRIVER FUNCTIONALITY------------#
#-----Libraries
import sys
#sys.path.insert(1, '\git\BikeLockSystem\Classes')
from Classes import BikeLockGPIO 
from Classes import BikeLockCamera 

#----- Variable Setup
BLGPIO = BikeLockGPIO.BLGPIO
BLCamera = BikeLockCamera.BLGPIO

print(BLGPIO.__str__(BLGPIO))
