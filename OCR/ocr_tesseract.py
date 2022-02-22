import numpy as np
import pytesseract, cv2, os
import matplotlib.pyplot as plt

PATH = r'C:\Users\Juhyun Lee\Desktop\깃헙\cv\OCR'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

os.chdir(PATH)

# Load Image
img = cv2.imread("Test.jpg", cv2.IMREAD_ANYCOLOR)
height, width, channel = img.shape

# Gray Scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
structingElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
imgTopHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, structingElement)
imgBlackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT,structingElement)
imgGrayslacePlusTopHat = cv2.add(gray, imgTopHat)
gray = cv2.subtract(imgGrayslacePlusTopHat, imgBlackhat)

# Gaussian Blur (noise)
img_blurred= cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)

# Adaptive Thresholding
img_thresh = cv2.adaptiveThreshold(
            img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 19,9)

contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    
contours_dict = []

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(temp_result, pt1=(x,y), pt2=(x+w, y+h), color=(255,255,255), thickness=2)

    contours_dict.append({
        'contour': contour,
        'x': x,
        'y': y,
        'w': w,
        'h': h,
        'cx': x+(w/2),
        'cy': y+(h/2)
    })

MIN_AREA, MAX_AREA = 80, 200
MIN_WIDTH, MIN_HEIGHT = 2, 8
MIN_RATIO, MAX_RATIO = 0.25, 1.0


possible_contours = []
x_y_pos = []
temp = []

for d in contours_dict:
    area = d['w']*d['h']
    ratio = d['w'] / d['h']

    if MIN_AREA < area < MAX_AREA and MIN_WIDTH < d['w'] and MIN_HEIGHT < d['h'] and MIN_RATIO < ratio < MAX_RATIO:
        possible_contours.append(d)
        x_y_pos.append([d['x'], d['y'], d['w'], d['h']])


x_y_pos.sort(key=lambda x:(x[0], x[1]))

for i in range(len(x_y_pos)-1):
    if abs(x_y_pos[i+1][0] - x_y_pos[i][0]) < 30 and abs(x_y_pos[i+1][1] - x_y_pos[i][1]) < 5:
        temp.append(x_y_pos[i])
        if i == len(x_y_pos)-2:
            temp.append(x_y_pos[i+1])

temp_result = np.zeros((height, width, channel), dtype=np.uint8)

for d in possible_contours:
    if [d['x'], d['y'], d['w'], d['h']] in temp:
        cv2.rectangle(img, pt1=(d['x'],d['y']), pt2=(d['x']+d['w'], d['y']+d['h']), color=(0,0,255), thickness=2)
        cv2.rectangle(temp_result, pt1=(d['x'],d['y']), pt2=(d['x']+d['w'], d['y']+d['h']), color=(255,255,255), thickness=2)

# Cropped Img = img[y:y+h, x:x+w]

dst_x, dst_y, dst_w, dst_h = np.inf, 0, 0, 0
for x, y, w, h in temp:
    if dst_x > x: dst_x = x
    if dst_y < y: dst_y = y
    if dst_w < w: dst_w = w
    if dst_h < h: dst_h = h

print(dst_x, dst_y, dst_w, dst_h)
# y:y+h, x:x+w
# result = img_thresh[dst_y:dst_y+dst_h, dst_x:dst_x+dst_w]
cv2.rectangle(img, pt1=(210,180), pt2=(310,150), color=(255,0,0), thickness=2)

result = img_thresh[150:180, 210:320]

# cv2.imshow("img", img)
# cv2.imshow("temp_result", temp_result)
# cv2.imshow("result", result)
# cv2.waitKey()
# cv2.destroyAllWindows()

config = ('-l kor+eng --oem 3 --psm 11')
string = pytesseract.image_to_string(result, config=config)
with open('ocr_result.txt', 'wt') as f:
    f.write(string)
