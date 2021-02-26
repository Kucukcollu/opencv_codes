#!/usr/bin/env python

import numpy as np
import cv2

def read_image(image_name):
    img=cv2.imread(image_name)
    fx=int(img.shape[1]/2)
    fy=int(img.shape[0]/2)
    d=(fx,fy)
    img=cv2.resize(img,d,interpolation=cv2.INTER_AREA)
    cv2.imshow("Original",img)
    return img

def color_filter(image,color_lover_bound,color_upper_bound):
    hsv_img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image format",hsv_img)

    mask=cv2.inRange(hsv_img,color_lover_bound,color_upper_bound)

    return mask

def get_contour(image_threshold):
    contours,hierarchy=cv2.findContours(image_threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    return contours


def draw_detect_contour(image_threshold,original_image,contour):
    black_image=np.zeros([image_threshold.shape[0],original_image.shape[1],3],"uint8")

    for c in contour:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)
        ((x,y),radius)=cv2.minEnclosingCircle(c)

        if area > 30000:
            cv2.drawContours(original_image,[c],-1,(150,250,150),-1)
            cv2.drawContours(black_image,[c],-1,(150,250,150),-1)

            cx,cy=get_contour_center(c)

            cv2.circle(original_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),5,(150,150,255),-1)
            print ("Area: {}, Perimeter: {}".format(area, perimeter))

    print ("number of contours: {}".format(len(contour)))
    cv2.imshow("RGB Image Contours",original_image)
    cv2.imshow("Black Image Contours",black_image)

    return black_image


def get_contour_center(contour):
    M=cv2.moments(contour)
    cx=-1
    cy=-1

    if M["m00"] != 0:
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
    
    return cx, cy

def main():
    image="/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball.jpg"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball2.jpg"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/shapes.png"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball3.jpg"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/basketball.jpg"

    yellow_lower =(30, 150, 100)
    yellow_upper = (50, 255, 255)

    img=read_image(image)
    img_threshold_mask=color_filter(img,yellow_lower,yellow_upper)
    contours=get_contour(img_threshold_mask)
    draw_detect_contour(img_threshold_mask,img,contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()
