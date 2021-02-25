#!/usr/bin/env python

import cv2
import numpy as np


# load original image
img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/shapes.png")
cv2.imshow("original",img)

# convert the original image to gray sacel image
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray_image)

# apply adaptive thresholding
binary_threshold=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
cv2.imshow("adaptive thresholding",binary_threshold)

# find contours
contours,hierarchy=cv2.findContours(binary_threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

"""
# draw the contours
cv2.drawContours(img,contours,-1,(255,0,255),2)
cv2.imshow("countered",img)
"""

# process
black_image=np.zeros([binary_threshold.shape[0],binary_threshold.shape[1],3],"uint8")

for c in contours:
    area=cv2.contourArea(c)
    perimeter=cv2.arcLength(c,True)
    ((x,y),radius) = cv2.minEnclosingCircle(c)
    cv2.drawContours(img,[c],-1,(150,250,150),1)
    cv2.drawContours(black_image,[c],-1,(150,250,150),1)
    M=cv2.moments(c)
    cx=-1
    cy=-1

    if M["m00"]!=0:
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])    
    
    cv2.circle(img,(cx,cy),(int)(radius),(0,0,255),1)
    cv2.circle(black_image,(cx,cy),(int)(radius),(0,0,255),1)
    print("Area:{}, Perimeter:{}".format(area,perimeter))
    
print("number of contours: {}".format(len(contours)))
cv2.imshow("rgb image",img)
cv2.imshow("black image",black_image)


while True:
    if cv2.waitKey(1) & 0xFF == 27 or cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
