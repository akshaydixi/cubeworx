import numpy as np
import cv2
import sys
colors = {'y' : [[25,100,100],[40,255,255]],
		  'o' : [[0,100,100],[25,255,255]],
		  'r' :    [[160,100,100],[180,255,255]],
		  'b' :   [[75,150,0],[140,255,255]],
		  'g' :  [[40,100,100],[75,255,255]]}
if sys.argv[1] not in colors:
	key = 'b'
else:
	key = sys.argv[1]


camera = cv2.VideoCapture('cube.mov')
while camera.isOpened():
	lower = np.array(colors[key][0],np.uint8)
	upper = np.array(colors[key][1],np.uint8)
	ret,img = camera.read()
	if ret:
		img = cv2.flip(img,1)
		frame = cv2.flip(img,1)

	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	separated = cv2.inRange(frame,lower,upper)

	contours,hierarchy = cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	max_area = 0
	largest_contour = None
	for idx,contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if area > max_area:
			largest_contour = contour
			if not largest_contour== None:
				moment = cv2.moments(largest_contour)
				if moment["m00"] > 1000:
					rect = cv2.minAreaRect(largest_contour)
					rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
					(width,height) = (rect[1][0],rect[1][1])
					print str(width) + " " + str(height)
					box = cv2.cv.BoxPoints(rect)
					box = np.int0(box)
					if(height > 0.9 * width and height < 1.1 * width):
						#cv2.drawContours(img,box,0,(0,0,255),2)
						pass
	cv2.imshow('img',separated)
	x = cv2.waitKey(1) & 0xFF
	if x == 27:
		print colors[key][0]
		break
	if x == 97:
		colors[key][0][1]-=1
	if x == 100:
		colors[key][0][1]+=1
	if x == 115:
		colors[key][0][2]-=1
	if x == 119:
		colors[key][0][2]+=1
		
camera.release()
cv2.destroyAllWindows()
