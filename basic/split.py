import cv2

# 채널 분리(split): 색상 공간의 채널을 b,g,r 단일 채널로 분리 
src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
b,g,r = cv2.split(src)
inverse = cv2.merge((r,g,b))

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("invers", inverse)

cv2.waitKey()
cv2.destroyAllWindows()