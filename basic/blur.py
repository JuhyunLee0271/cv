import cv2

# 흐림효과(blur): 영상이나 이미지를 번지게 함, 노이즈를 제거해 연산 시 계산을 빠르고 정확하게 수행할 수 있음
# 단순 흐림 효과는 각 픽셀에 대해 커널을 적용해 모든 픽셀의 평균을 구하는 연산 
src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
dst = cv2.blur(src, (9,9), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()