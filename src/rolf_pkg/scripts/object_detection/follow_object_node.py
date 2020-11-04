#!/usr/bin/env python

import rospy
from objectDetectionModule import *
from cv_bridge import CvBridge

from sensor_msgs.msg import Image
from rolf_pkg.msg import ControlRequest

bridge = CvBridge()
readParams()

def readParams():
    global pubResImg = rospy.get_param('publishResultImage', True)

def callbackImage(sub_img):
    cv_img = bridge.imgmsg_to_cv2(sub_img, desired_encoding='passthrough')
    result_im, objectInfo = getObjects(cv_img, 0.5, 0.1, pubResImg)

    if pubResImg:
        pub_img = bridge.cv2_to_imgmsg(result_im, encoding="passthrough")
        msg = Image()
        msg.header = sub_img.header
        pub.publish(msg)

    # ctrlRqst = ControlRequest()

def followObject():
    rospy.init_node('motor_driver', anonymous=True)
    sub = rospy.Subscriber("raspicam_node/image/compressed", Image, callbackImage)
    pub = rospy.Publisher('rolf/control_request', ControlRequest, queue_size=1)

    rospy.spin()

if __name__ == '__main__':
    followObject()
