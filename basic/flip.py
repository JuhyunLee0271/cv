import cv2

image = cv2.imread('tree.jpg', cv2.IMREAD_ANYCOLOR)
image = cv2.resize(image, (1200,800))
dst = cv2.flip(image, 0)

cv2.imshow("Tree_2", image)
cv2.imshow("Tree_1", dst)
cv2.waitKey()
cv2.destroyAllWindows()