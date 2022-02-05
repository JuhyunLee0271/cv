import cv2

# 카메라 출력
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# q가 입력될 때까지 카메라 출력
while cv2.waitKey(33) != ord('q'):
    ret, frame = cap.read()
    cv2.imshow("VideoFrame", frame)

cap.release()
cv2.destroyAllWindows()