import cv2

# 이미지 출력 
image = cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR)
image = cv2.resize(image, (1200,800))
cv2.imshow("Moon", image)
height, width, channel = image.shape
print(height, width, channel)
cv2.waitKey()
cv2.destroyAllWindows()