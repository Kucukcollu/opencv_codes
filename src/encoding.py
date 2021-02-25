#!/usr/bin/env python

import numpy as np
import cv2

# read the image as "img"
img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/wall_e.jpg",cv2.IMREAD_COLOR)

# show the original image
cv2.imshow("original",img)
cv2.moveWindow("original",0,0)

print("shape of the original image: ",img.shape)

height,width,channel=img.shape

# BGR Format
blue,green,red=cv2.split(img)

# blue
cv2.imshow("blue",blue)
cv2.moveWindow("blue",0,height+200)

# green
cv2.imshow("green",green)
cv2.moveWindow("green",width+200,0)

# red
cv2.imshow("red",red)
cv2.moveWindow("red",width+200,height+200)


# HSV Format
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
hsv_img=np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv format",hsv_img)


# GRAY Format
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray format",gray_img)

while True:
    if cv2.waitKey(10) & 0xFF == 27 or cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
