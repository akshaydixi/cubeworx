import numpy as np
import cv2

camera = cv2.VideoCapture(0)
BLUE_MIN = np.array([100,150,0],np.uint8)
BLUE_MAX = np.array([140,255,255],np.uint8)

while camera.isOpened():
    ret,frame = camera.read()
    if ret:
        frame = cv2.flip(frame,1)

    """ b,g,r = cv2.split(frame)
    r = r-(b+g)
    r = cv2.merge((b-b,g-g,r-(b+g)))
    red = cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(red,50,255,0)
    """
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(frame,BLUE_MIN,BLUE_MAX)
    thresh = cv2.medianBlur(thresh,5) 
    cv2.imshow('red',thresh)
    if cv2.waitKey(1) & 0xFF == 27:
        break
camera.release()
cv2.destroyAllWindows()
