#!/usr/bin/env python

import numpy as np
import cv2

cam_capture=cv2.VideoCapture(0)

while(True):
    ret,frame=cam_capture.read()

    if not ret:
        print("Camera cannot be used!")
        break
    
    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    binary_threshold=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
    contours,hierarchy=cv2.findContours(binary_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(frame,contours,-1,(255,0,255),2)
    
    cv2.imshow("camera",frame)
    cv2.imshow("gray image",gray_image)
    cv2.imshow("adaptive thresholding",binary_threshold)
    cv2.imshow("countered",frame)

    if cv2.waitKey(10)&0xFF==ord("q"):
        break

cam_capture.release()
cv2.destroyAllWindows()
