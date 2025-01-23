#--------------CAMERA FUNCTIONALITY------------#

#-----Libraries
from time import sleep       
#from picamera2 import Picamera2, Preview
#from libcamera import Transform 


#--Class Init
class BLCamera:
    
    def __init__(self):
        picam2 = Picamera2()
    def __str__(self):
        return "I am GPIO"

#-----Functions
    def RecordTenSecondVideo():
        picam2.start_preview(Preview)

        #preview_config = picam2.create_preview_configuration()
        #picam2.configure(preview_config)

        picam2.start_and_record_video("TestBikeLockVideo.mp4", duration = 10, show_preview = True) #records a 10 second video
        picam2.close()
