import numpy as np
import cv2
import operator
import sys
minVal = 100
maxVal = 200
colors = {'y' : [[25,100,100],[40,255,255],[25,200,25]],
          'o' : [[0,100,100],[25,255,255],[100,220,20]],
          'r' :    [[160,100,100],[180,255,255],[0,0,255]],
          'b' :   [[75,100,100],[140,255,255],[255,0,0]],
          'g' :  [[40,100,100],[75,255,255],[0,255,0]]}


camera = cv2.VideoCapture('cube.mov')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))
while camera.isOpened():
    ret,_frame = camera.read()
    _frame = cv2.medianBlur(_frame,5)
    
    gray = cv2.cvtColor(_frame,cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    
    #thresh = cv2.erode(thresh,kernel,iterations=1)
    #thresh = cv2.dilate(thresh,kernel,iterations=1)
    thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
    canny = thresh#cv2.Canny(thresh,minVal,maxVal)
    
    contours,hierarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    largests = []
    for cnt in contours:
        largests.append((cv2.contourArea(cnt),cnt))
    largests.sort(key=operator.itemgetter(0))
    largests.reverse()
    meanarea = 0
    for cnt in largests[:10]:
        meanarea +=cnt[0]
    meanarea = meanarea/10
    for cnt in largests[:15]:
        if cnt[0] > meanarea * 1.1 or cnt[0] < meanarea*0.9:continue    
        x,y,w,h = cv2.boundingRect(cnt[1])
        cv2.rectangle(canny,(x,y),(x+w,y+h),(255,255,250),10)
    """
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

    
    """
    if not ret:
        break
    cv2.imshow('img',canny)
    x = cv2.waitKey(1) & 0xFF
    if x == 27:
        print minVal,maxVal
        break
    if x == 81:
        minVal-=30
        print 'left'
    if x == 82:
        maxVal+=30
        print 'up'
    if x == 83:
        minVal+=30
        print 'right'
    if x == 84:
        maxVal-=30
        print 'down'
    
camera.release()
cv2.destroyAllWindows()

