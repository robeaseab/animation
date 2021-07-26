

from picamera import PiCamera
from time import sleep
from gpiozero import Button
import os
from datetime import time, tzinfo, timedelta, datetime

#os.mkdir('/media/pi/34B3-2752/test_dir')
now = str(datetime.now())
time_dir = now.replace(" ","_").replace(":",".")
path = time_dir
print(path)
os.mkdir(path)


button = Button(17)
camera = PiCamera()
camera.rotation = 180

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        # camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        camera.capture(path + '/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break

# camera.start_preview()
# button.wait_for_press()
# sleep(3)
# camera.capture('/media/pi/34B3-2752/animation/image.jpg')
# camera.stop_preview()

