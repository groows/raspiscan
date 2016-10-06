import picamera
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

#camera.start_recording('video.h264')
#sleep(5)
#camera.stop_recording()
camera.capture('image2.jpg')
