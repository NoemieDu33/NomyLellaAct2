from PIL import Image,ImageEnhance
from tesserocr import PyTessBaseAPI, PSM
#pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe" #"/usr/bin/tesseract"
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
    images = ['u.jpg', 'h.jpg', 's.jpg']

    with PyTessBaseAPI(psm=PSM.SINGLE_CHAR,path="C:/Program Files/Tesseract-OCR/tessdata") as api:
        for img in images:
            api.SetImageFile(img)
            print (f"{api.GetUTF8Text()[0]} - conf:{api.AllWordConfidences()[0]}")


letterimg()
