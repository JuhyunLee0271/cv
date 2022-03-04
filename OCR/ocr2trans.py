import pytesseract,os,cv2
from googletrans import Translator

"""
OCR2Trans
    - OCR2Trans can be used to translate after optical character recognition(OCR) in an image. (pytesseract, googletrans)
    - You can change pytesseract's config (@self.config) such as (-l eng+kor --oem 3 --psm 7)
    - You can also change googletrans's config such as (src='ko' dest='en')
    - Work Flow is as follows.
        Image Load -> Image Processing -> OCR(pytesseract) -> Translate(googletrans)
"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class OCR2Trans:

    def __init__(self):
        self.config = ('-l eng --oem 3 --psm 4')
        self.img = None
        self.string = None
        self.result = None
        self.PATH = r'C:\Users\Juhyun Lee\Desktop\깃헙\cv\OCR'
        self.translator = Translator()

        os.chdir(self.PATH)

    def loadImage(self, img):
        self.img = cv2.imread(img, cv2.IMREAD_ANYCOLOR)

    def run(self):
        self.imageProcess()
        self.OCR()
        self.translate()

    def imageProcess(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        structingElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        imgTopHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, structingElement)
        imgBlackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT,structingElement)
        imgGrayslacePlusTopHat = cv2.add(gray, imgTopHat)
        gray = cv2.subtract(imgGrayslacePlusTopHat, imgBlackhat)

        img_blurred = cv2.GaussianBlur(gray, ksize=(5,5), sigmaX=0)
        
        self.img = img_blurred

    def OCR(self):
        string = pytesseract.image_to_string(self.img, config=self.config)
        string = string.replace('\n', ' ').split('.')        
        self.string = string
    
    # need language mapping
    def translate(self):
        result = ""
        for s in self.string:
            if len(s) == 1: continue
            result += self.translator.translate(s, src='en', dest='ko').text + "\n"
        self.result = result
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(result)

if __name__ == "__main__":
    ocr = OCR2Trans()
    ocr.loadImage('testocr.png')
    ocr.run()

