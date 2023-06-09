import time
time_import_begin = time.time()
import pytesseract
import sys, os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from functools import cache
time_import_end = time.time()
print(time_import_end - time_import_begin)
print("debut boucle")

pytesseract.pytesseract.tesseract_cmd='/usr/bin/tesseract'


HOST = "10.3.141.100"  # The server's hostname or IP address
PORT = 5050  # The port used by the server


while True:
	if not len(os.listdir('/home/jevaisdevenirfolle/Desktop/output')):
		time.sleep(1)
	else:
		time_main_begin = time.time()
		im = Image.open('/home/jevaisdevenirfolle/Desktop/output/H.jpg').convert('RGBA')
		#im = im.rotate(90)
		im = im.convert('L')
		im = ImageEnhance.Brightness(im).enhance(3) #augmenter enhance si luminosité faible ! 
		im = im.point(lambda x: 0 if x<140 else 255)
		im.save("ghughei.jpg")
		time_main_end=time.time()
		print(time_main_end - time_main_begin)
		text = pytesseract.image_to_string(im, config="-l eng --oem 3 --psm 10 -c tessedit_char_whitelist=hsuHSU")
		print(text)
	
