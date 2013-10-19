import numpy as np
import cv2
import sys

colors = {'y' : [[25,100,100],[40,255,255],[25,200,25]],
          'o' : [[0,100,100],[25,255,255],[100,220,20]],
          'r' :    [[160,100,100],[180,255,255],[0,0,255]],
          'b' :   [[75,100,100],[140,255,255],[255,0,0]],
          'g' :  [[40,100,100],[75,255,255],[0,255,0]]}

if sys.argv[1] not in colors or len(sys.argv)!=2:
    key = 'b'
else:
    key = sys.argv[1]

camera = cv2.VideoCapture('cube.mov')
lower = np.array(colors[key][0],np.uint8)
upper = np.array(colors[key][1],np.uint8)
while camera.isOpened():
    ret,_frame = camera.read()
    frame = _frame.copy()
    frame = cv2.blur(frame,(3,3))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(colors[color][0],np.uint8)
        upper = np.array(colors[color][1],np.uint8)
        thresh = cv2.inRange(hsv,lower,upper)
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cubes = []
        maxarea = 0
        allareas = []
        try:
            biggestcontour = contours[0]
        except:
            pass
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > maxarea:
                allareas.append(area)
                maxarea = cv2.contourArea(contour)
                biggestcontour = contour
        allareas.sort()
        try:
            maxarea = (allareas[-1] + allareas[-2] + allareas[-3]) / 3.0
        except:
            maxarea = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 0.9 * maxarea and area < 1.1 * maxarea:
                cubes.append(contour)
        for cube in cubes:
            x,y,w,h = cv2.boundingRect(cube)
            cv2.rectangle(frame,(x,y),(x+w,y+h),colors[color][2],2)

    
    
    if not ret:
        break
    cv2.imshow('img',frame)
    x = cv2.waitKey(1) & 0xFF
    if x == 27:
        break
    if x == 81:
        print 'left'
    if x == 82:
        print 'up'
    if x == 83:
        print 'right'
    if x == 84:
        print 'down'
    
camera.release()
cv2.destroyAllWindows()

