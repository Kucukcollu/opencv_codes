#!/usr/bin/env python

import numpy as np
import cv2

img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/penguin.jpg")

cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

cv2.imshow("Image",img)

cv2.waitKey(0)

cv2.imwrite("/home/ronux/catkin_ws/src/opencv_codes/copy/copied_penguin.jpg",img)
