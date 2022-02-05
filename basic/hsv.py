import cv2

# HSV: HSV 공간은 색상을 표현하기 위한 간편한 색상 공간
# H(색상), S(채도), V(명도)
src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)

cv2.waitKey()
cv2.destroyAllWindows()