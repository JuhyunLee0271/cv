import cv2

cap = cv2.VideoCapture('bumproad.mp4')

# Video가 끝나면 처음부터 다시 시작
while cv2.waitKey(33) != ord('q'):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    cv2.imshow("VideoFrame", frame)

cap.release()
cv2.destroyAllWindows()

