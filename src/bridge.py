#!/usr/bin/env python

"""
CvBridge: translation between ROS and OpenCv
"""

import rospy
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# create object
bridge=CvBridge()

def image_callback(ros_image):

    print("got an image")
    global bridge

    # convert image to OpenCv format
    try:
        cv_image=bridge.imgmsg_to_cv2(ros_image,"bgr8")
    except CvBridgeError:
        print("error")
    
    # it is done now test it

    (rows,cols,channels)=cv_image.shape
    
    if cols>200 and rows>200:
        cv2.circle(cv_image,(100,100),90,255)
    
    cv2.putText(cv_image,"webcam activated",(10,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("image",cv_image)
    
    cv2.waitKey(3)

def main(args):

    rospy.init_node("image_converter",anonymous=True)

    #image_topic="/usb_cam/image_raw"
    image_sub=rospy.Subscriber("/usb_cam/image_raw",Image,image_callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv)
