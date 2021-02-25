#!/usr/bin/env python

import numpy as np
import cv2

img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/wall_e.jpg")
gray_img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/wall_e.jpg",cv2.IMREAD_GRAYSCALE)
ret,threshold_basic=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
adaptive_thresholding=cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,127,2)

cv2.imshow("original",img)
cv2.imshow("gray",gray_img)
cv2.imshow("basic thresholding",threshold_basic)
cv2.imshow("adaptive thresholding",adaptive_thresholding)

while True:
    if cv2.waitKey(10) & 0xFF == 27 or cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
