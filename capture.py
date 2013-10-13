import cv2

camera = cv2.VideoCapture(0)


while camera.isOpened():
    ret,frame = camera.read()
    if cv2.waitKey == 27:
        cv2.imwrite(frame,'cube.jpg')
        break
camera.release()
cv2.destroyAllWindows()
