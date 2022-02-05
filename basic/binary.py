import cv2

# 이진화(binary): 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 대상 값을 대상으로 특정 연산을 수행
# 기준 값에 따라 참 또는 거짓으로 나누는 이분법적 연산

src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
# 그레이스케일 이미지에 대해 이진화 함수(threshold) 적용.
# 픽셀이 60을 초과한 경우 255, 그렇지 않은 경우 0 으로 변경 
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()