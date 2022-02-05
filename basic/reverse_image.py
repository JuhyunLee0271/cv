import cv2

# 역상(Reverse Image): 영상이나 이미지를 반전 된 색상으로 변환하기 위해 사용
# 비트연산 NOT 적용 

src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
dst = cv2.bitwise_not(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()
