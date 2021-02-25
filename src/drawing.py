#!/usr/bin/env python

import numpy as np
import cv2

img=np.zeros((512,512,3),dtype=np.uint8)

cv2.line(img,(0,0),(200,200),(255,255,255),5)

cv2.rectangle(img,(384,0),(500,128),(0,255,0),3)

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow("shape",img)

while True:
    if cv2.waitKey(10) & 0xFF == 27 or cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
