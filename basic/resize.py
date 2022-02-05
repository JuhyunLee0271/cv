import cv2

src = cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR)

# 절대 크기 변경(임의의 크기 (width, height)로 변경)
# 상대 크기 변경(이미지의 크기를 비율에 맞게 변경)
dst = cv2.resize(src, dsize=(600,400), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()
