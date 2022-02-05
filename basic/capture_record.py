import cv2
from datetime import datetime

capture = cv2.VideoCapture('bumproad.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open('bumproad.mp4')
    
    ret, frame = capture.read()
    cv2.imshow('frame', frame)

    now = datetime.now().strftime("%d_%H_%M_%S")
    key = cv2.waitKey(33)

    if key == 27:
        break
    
    elif key == 26:
        print("캡쳐")
        cv2.imwrite(str(now) + ".png", frame)
    
    elif key == 24:
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter(str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    
    elif key == 3:
        print("녹화 중지")
        record = False
        capture.release()

    if record == True:
        print("녹화 중")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()