import numpy as np
import cv2
import sys
args = sys.argv
if len(args) != 2:
    src = 0
else:
    if args[1] == 'cube':
        src = 'cube.mov'
    else:
        src=0
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret,frame = camera.read()
    if not ret:
        break
    
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img,(4,4))
    ret,thresh = cv2.threshold(img,120,255,0)
    contours, hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,0,0),-1)
    #for contour in contours:
    #    x,y,w,h, = cv2.boundingRect(contour)
    #    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    cv2.imshow('img',img)
    
    x = cv2.waitKey(1) & 0xFF
    if x == 27:
        break

camera.release()
cv2.destroyAllWindows()
