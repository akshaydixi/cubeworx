import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret,frame = camera.read()
    if ret:
        frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()
