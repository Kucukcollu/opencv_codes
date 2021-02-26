#!/usr/bin/env python

import numpy as np
import cv2

cam_capture=cv2.VideoCapture(0)

while(True):
    ret,frame=cam_capture.read()
    
    if not ret:
        print("Camera cannot be used!")
        break
    
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    threshold_value,threshould = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
    print("Threshold value:",threshold_value)
    cv2.imshow("camera",threshould)

    if cv2.waitKey(10)&0xFF==ord("q"):
        break

cam_capture.release()
cv2.destroyAllWindows()
