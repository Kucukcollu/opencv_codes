#!/usr/bin /env python

import cv2

camera=cv2.VideoCapture(0)

while True:
    ret,frame=camera.read()
    
    if not ret:
        print("Camera error!")
        break
    
    # change the format from BGR to HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",hsv)


    # describe the upper and lower limits
    red_lower=(0,50,100)
    red_upper=(30,255,255)

    # define a mask with using lower and upper bounds
    mask=cv2.inRange(hsv,red_lower,red_upper)
    cv2.imshow("mask",mask)

    if cv2.waitKey(10)&0xFF==27 or cv2.waitKey(10)&0xFF==ord("q"):
        break

if camera.isOpened():
    camera.release()

cv2.destroyAllWindows()
