import time
from PIL import Image, ImageChops, ImageFilter,ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe" #"/usr/bin/tesseract"
import numpy as np
import cv2
from functools import cache
#import takepic


lettres = {
"U" : ["U","u","Y","y","O","o","V","v","0","J","j","7"],
"H" : ["H","h","M","m","N","n","K","k","X","x","I","i","1","A","a"],
"S" : ["S","s","Z","z","2","C","c","3","5"]
}

@cache
def letterimg()->None:
	#takepic.prendre_photo()
	print("Done!")
	img = Image.open("s.jpg") 

	enhancer = ImageEnhance.Brightness(img)
	img = enhancer.enhance(2)
	img.save("SA_image.jpg")
	img = Image.open("SA_image.jpg")
	bw = img.convert('1',dither=Image.NONE)
	bw = bw.resize((2000,2000))

	bw.save("BW_image.jpg")
	print("BW saved")

	#img = Image.open(filename) 
	#bw = img.filter(ImageFilter.UnsharpMask(radius=6.8, percent=269, threshold =0))

	img = np.array(Image.open("BW_image.jpg"))

	text = pytesseract.image_to_string(img,config="-l eng --oem 3 --psm 10 -c tessedit_char_whitelist=hsuHSU")




	print(f"Resultat (raw) : {text}")
	text = text[0]
	for k,v in lettres.items():
		if text in str(v):
			text = k
			break
	print(f"Resultat (choix 1) : {text.upper()}")
    

letterimg()
input()
