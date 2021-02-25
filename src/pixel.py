#!/usr/bin/env python

import numpy as np
import cv2

# read the image as "img"
img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/penguin.jpg")

# show the "img" as matrix shape
print("image: ",img)

# show the type of the "img"
print("type: ",type(img))

# size
print("size: ",img.size)

# shape
print("shape: ",img.shape)

# image shape as w,l,c
print("width: ",img.shape[0])
print("length: ",img.shape[1])
print("channel: ",img.shape[2])

# length
print("length: ",len(img))

# data type
print("dtype: ",img.dtype)

# choose a random pixel value
print("pixel value:",img[200][800])

# row
print("row: ",img[20])

# read second channel
print("second channel: ",img[:,:,2])
