#L10-Server web cu control vizual3
#import picamera
#camera=picamera.PiCamera()

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

GPIO.output(3,0)
#camera.capture("/var/www/html/imag1.jpg")
