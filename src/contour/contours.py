#!/usr/bin/env python

import numpy as np
import cv2

def read_image(image_name):
    img=cv2.imread(image_name)
    cv2.imshow("Original",img)
    return img

def convert_img_to_gray(image,blur):
    gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray image",gray_img)
    
    if blur:
        img=cv2.GaussianBlur(image,(5,5),0)
    
    return gray_img

def apply_threshold(gray_image):
    img_threshold=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
    cv2.imshow("Adaptive threshold",img_threshold)

    return  img_threshold

def get_contour(image_threshold):
    contours,hierarchy=cv2.findContours(image_threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    return contours

def draw_contours(image,contours,image_name):
    pass

def process_contours(image_threshold,original_image,contour):
    black_image=np.zeros([image_threshold.shape[0],original_image.shape[1],3],"uint8")

    for c in contour:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)
        ((x,y),radius)=cv2.minEnclosingCircle(c)

        if area > 10:
            cv2.drawContours(original_image,[c],-1,(150,250,150),-1)
            cv2.drawContours(black_image,[c],-1,(150,250,150),-1)

            cx,cy=get_contour_center(c)

            cv2.circle(original_image, (cx,cy),(int)(radius),(0,0,255),1)
            cv2.circle(black_image, (cx,cy),(int)(radius),(0,0,255),1)
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
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball.jpg"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball2.jpg"
    image="/home/ronux/catkin_ws/src/opencv_codes/images/shapes.png"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/tennis_ball3.jpg"
    #image="/home/ronux/catkin_ws/src/opencv_codes/images/basketball.jpg"
    img=read_image(image)
    gray_img=convert_img_to_gray(img,blur=True)
    img_threshold=apply_threshold(gray_img)
    contours=get_contour(img_threshold)
    process_contours(img_threshold,img,contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()
