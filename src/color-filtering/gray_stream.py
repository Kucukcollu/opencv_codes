#!/usr/bin/env python

import numpy as np
import cv2

cam_capture=cv2.VideoCapture(0)

while(True):
    ret,frame=cam_capture.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera",frame)

    if cv2.waitKey(10)&0xFF==ord("q"):
        break

cam_capture.release()
cv2.destroyAllWindows()
