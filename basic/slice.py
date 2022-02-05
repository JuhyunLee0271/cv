import cv2

# Slice: 영상이나 이미지에서 특정 영역을 잘라내는 연산
# 관심영역(ROI): 객체를 탐지하거나 검출하는 영역
# Numpy의 배열 형식과 동일하므로 행과 열을 자름
src = cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR)
dst = src[100:600, 200:700].copy()

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

src = cv2.resize(cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR), (1200,800))
roi = src[300:800, 100:600].copy()
src[0:500, 0:500] = roi

cv2.imshow("src", src)

cv2.waitKey()
cv2.destroyAllWindows()
