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

while True:
	if not len(os.listdir('/home/jevaisdevenirfolle/Desktop/output')):
		time.sleep(1)
	else:
		time_main_begin = time.time()
		time.sleep(0.1)
		im = Image.open('/home/jevaisdevenirfolle/Desktop/output/H.jpg').convert('RGBA')
		#im = im.rotate(90)
		im = im.convert('L')
		im = ImageEnhance.Brightness(im).enhance(1) #augmenter enhance si luminosité faible ! 
		im = im.point(lambda x: 0 if x<140 else 255)
		im.save("ghughei.jpg")
		time_main_end=time.time()
		print(time_main_end - time_main_begin)
		
		text = pytesseract.image_to_string(im, config="-l eng --oem 3 --psm 10 -c tessedit_char_whitelist=hsuHSU")
		print(text)
		os.remove('/home/jevaisdevenirfolle/Desktop/output/H.jpg')
	
