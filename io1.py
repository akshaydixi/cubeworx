import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('len.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img2)
plt.show()
cv2.imshow('bgr',img)
cv2.imshow('rgb',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
