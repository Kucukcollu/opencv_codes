#!/usr/bin/env python

import numpy as np
import cv2
import imutils

img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball.jpg")

fx=int(img.shape[1]/4)
fy=int(img.shape[0]/4)
dim=(fx,fy)

img=cv2.resize(img,dim,fx=fx,fy=fy,interpolation=cv2.INTER_AREA)
cv2.imshow("original",img)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image",hsv)

yellow_lower=(30,80,10)
yellow_upper=(60,255,255)

# define a mask with using lower and upper bounds
mask=cv2.inRange(hsv,yellow_lower,yellow_upper)
cv2.imshow("mask",mask)


while True:
    if cv2.waitKey(10) & 0xFF == 27 or cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
