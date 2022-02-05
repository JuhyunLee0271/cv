import cv2

src = cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR)

# height, width를 이용한 회전 중심점
height, width, channel = src.shape
# 회전 변환 행렬 (중심점, 각도, 비율)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
# Affine 변환 함수로 회전 변환을 계산
dst = cv2.warpAffine(src, matrix, (width, height))

src = cv2.resize(src, (1200,800))
dst = cv2.resize(dst, (1200,800))

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()