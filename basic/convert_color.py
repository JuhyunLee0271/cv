import cv2

# 색상 공간 변환(Convert color): 본래의 색상 공간에서 다른 색상 공간으로 변환할 때 사용
# COLOR_BGR2GRAY: RGB -> GRAY

src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()