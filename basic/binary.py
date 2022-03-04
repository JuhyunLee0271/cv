import cv2

# 이진화(binary): 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 대상 값을 대상으로 특정 연산을 수행
# 기준 값에 따라 참 또는 거짓으로 나누는 이분법적 연산

src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
# 그레이스케일 이미지에 대해 이진화 함수(threshold) 적용.
# 픽셀이 60을 초과한 경우 255, 그렇지 않은 경우 0 으로 변경 
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)
th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)


cv2.imshow("gray", gray)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
# cv2.imshow("th2", th2)
# cv2.imshow("th3", th3)

cv2.waitKey()
cv2.destroyAllWindows()