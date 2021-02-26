#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def image_callback(ros_image):

    bridge=CvBridge()

    # convert image to OpenCv format
    cv_image=bridge.imgmsg_to_cv2(ros_image,"bgr8")

    # it is done now test it
    cv2.imshow("image",cv_image)
    cv2.waitKey(3)

def main():
    rospy.init_node("image_converter",anonymous=True)
    image_sub=rospy.Subscriber("/usb_cam/image_raw",Image,image_callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
