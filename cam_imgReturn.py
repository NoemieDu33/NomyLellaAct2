import time
init1=time.time()
from PIL import Image, ImageChops,ImageEnhance
init2=time.time()
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
init3=time.time()
import numpy as np
init4=time.time()
from functools import cache
import takepic
init6=time.time()

print(f"""
import PIL : {round(init2-init1,3)}s
import Tesseract : {round(init3-init2,3)}s
import Numpy : {round(init4-init3,3)}s
import Functools : {round(init6-init4,3)}s
Temps total : {round(init6-init1,3)}s
""")
lettres = {
"U" : ["U","u","Y","y","O","o","V","v","0","J","j","7"],
"H" : ["H","h","M","m","N","n","K","k","X","x","I","i","1","A","a"],
"S" : ["S","s","Z","z","2","C","c","3","5"]
}

def trim(im):
	bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
	diff = ImageChops.difference(im,bg)
	diff = ImageChops.add(diff, diff, 2.0, -100)
	bbox = diff.getbbox()
	if bbox:
		return im.crop(bbox)

@cache
def letterimg()->None:
	initi = time.time()
	takepic.prendre_photo()
	
	print("Done!")
	img = Image.open("detection.jpg") 
	print(f"""Image.open : {round(time.time()-initi,3)}s""")

	initi=time.time()
	enhancer = ImageEnhance.Brightness(img)
	img = enhancer.enhance(4)
	basewidth = 2000
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize))
	img.save("SA_image.jpg")
	img = Image.open("SA_image.jpg")
	bw = img.convert('1',dither=Image.NONE)
	print(f"""img.convert : {round(time.time()-initi,3)}s""")

	initi=time.time()
	bw.save("BW_image.png")
	print("BW saved")
	img = Image.open("BW_image.png").convert('RGBA')
	img = img.rotate(90)
	
	#img = trim(img)
	img.save("SW_image.png")
	print("SW saved")
	print(f"""bw.save : {round(time.time()-initi,3)}s""")

	#initi=time.time()
	#img = Image.open(filename) 
	#bw = img.filter(ImageFilter.UnsharpMask(radius=6.8, percent=269, threshold =0))
	#print(f"""cv2.imread : {round(time.time()-initi,3)}s""")

	initi=time.time()
	img = np.array(Image.open("SW_image.png"))
	print(f"""np.array : {round(time.time()-initi,3)}s""")

	initi=time.time()
	text = pytesseract.image_to_string(img,config="-l eng --oem 3 --psm 10 -c tessedit_char_whitelist=hsuHSU")

	print(f"""tesseract img to string : {round(time.time()-initi,3)}s""")  



	initi=time.time()
	print(f"Resultat (raw) : {text}")
	text = text[0]
	for k,v in lettres.items():
		if text in str(v):
			text = k
			break
		
	return text.upper()
    
