#!/usr/bin/env python

import cv2

# load image as "img"
img=cv2.imread("/home/ronux/catkin_ws/src/opencv_codes/images/penguin.jpg")

# show the "img"
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)

# close when "ESC" or "q" buttons pressed
while True:
    if cv2.waitKey(10) & 0xFF == 27 or cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

# saved the "img" as ...
cv2.imwrite("/home/ronux/catkin_ws/src/opencv_codes/copy/copied_penguin.jpg",img)
