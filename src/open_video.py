#!/usr/bin/env python

import numpy as np
import cv2

video_cap=cv2.VideoCapture("/home/ronux/catkin_ws/src/opencv_codes/videos/traffic.mp4")

while(True):
    ret,frame=video_cap.read()
    
    cv2.imshow("Traffic",frame)
    
    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

video_cap.release()
cv2.destroyAllWindows()
