import cv2

# 이미지 피라미드(Image pyramid)를 활용해 확대와 축소의 샘플링을 거침, 2배로 확대하거나 축소하는 것만 가능 
# 확대: 업 샘플링, 축소: 다운 샘플링

src = cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR)
height, width, channel = src.shape

# pyrUp: 업 샘플링, pyrDown: 다운 샘플링 
dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()