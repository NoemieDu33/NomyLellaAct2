from picamera2 import Picamera2, Preview
import time

def prendre_photo():
	picam2 = Picamera2()
	config = picam2.create_still_configuration()#main={"size":(1920,1080)}, lores={"size":(640,480)}, display="lores"
	picam2.configure(config)
	picam2.start_preview(Preview.QTGL)
	picam2.start()
	time.sleep(2)
	picam2.capture_file("detection.jpg")
