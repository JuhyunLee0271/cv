import cv2, sys, os
import numpy as np

# Using Haar Cascade from OpenCV - a classifier that is used to identify specific objects from a source image.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors = 5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        cv2.imshow("Face detector", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()




