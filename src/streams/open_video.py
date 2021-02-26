#!/usr/bin/env python

import numpy as np
import cv2

video_cap=cv2.VideoCapture("/home/ronux/catkin_ws/src/opencv_codes/videos/traffic.mp4")

while(True):
    ret,frame=video_cap.read()
    
    frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    threshold_value,threshould = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
    print("Threshold value:",threshold_value)
    cv2.imshow("camera",threshould)
    
    if cv2.waitKey(1) & 0xFF == 27 or cv2.waitKey(1) & 0xFF == ord("q"):
        break

if video_cap.isOpened():
    video_cap.release()

cv2.destroyAllWindows()
