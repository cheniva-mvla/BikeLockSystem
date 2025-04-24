#--------------CAMERA FUNCTIONALITY------------#
safeLock = True #Toggle for working on and off Raspberry Pi. 

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

#----- Init 
    def __init__(self):
        pass

#----- Getters and Setters
    def getSafeLock(self):
        return safeLock
       
#----- Logic Functions
    def TakePicture(self):
        if safeLock:
            self.picam2.capture_file("BikeLockImage.jpg")
            self.picam2.close()
    def RecordTenSecondVideo(self): #records a 10 second video
        if safeLock:
            #self.picam2.start_preview(Preview.QTGL)

            #preview_config = picam2.create_preview_configuration()
            #picam2.configure(preview_config)

            self.picam2.start_and_record_video("TestBikeLockVideo.mp4", duration = 30, show_preview = True) 
            self.picam2.close()

#----- Misc
    def __str__(self):
        return "CAMERA CLASS"