#--------------CAMERA FUNCTIONALITY------------#
safeLock = False #Toggle for working on and off Raspberry Pi. 

#-----Libraries
if safeLock:
    from time import sleep       
    from picamera2 import Picamera2, Preview
    from libcamera import Transform 
else:
    from time import sleep       


#--Class Init
class BLCamera:
    if safeLock:
        picam2 = Picamera2()

    #init
    def __init__(self):
        pass

    #toString  
    def __str__(self):
        return "I am Camera"

    #-----Functions
    def RecordTenSecondVideo(self):
        if safeLock:
            self.picam2.start_preview(Preview)

            #preview_config = picam2.create_preview_configuration()
            #picam2.configure(preview_config)

            self.picam2.start_and_record_video("TestBikeLockVideo.mp4", duration = 10, show_preview = True) #records a 10 second video
            self.picam2.close()

