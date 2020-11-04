#!/usr/bin/env python

import rospy
from objectDetectionModule import *
from cv_bridge import CvBridge

from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from rolf_pkg.msg import ControlRequest

bridge = CvBridge()
pubCtrlRqst = rospy.Publisher('rolf/control_request', ControlRequest, queue_size=1)
pubImg = rospy.Publisher('rolf/img_objects', Image, queue_size=10)

# readParams()

# def readParams():
#     global pubResImg
#     pubResImg = True #rospy.get_param('~/publishResultImage', True)

def callbackImage(sub_img):
    cv_img = bridge.compressed_imgmsg_to_cv2(sub_img)
    result_im, objectInfo = getObjects(cv_img, 0.5, 0.1, True)
    
    if True:
        #pub_img = bridge.cv2_to_compressed_imgmsg(result_im, dst_format='jpg')
        pub_img = bridge.cv2_to_imgmsg(result_im, encoding="passthrough")
        pub_img.header = sub_img.header
        pubImg.publish(pub_img)

    # ctrlRqst = ControlRequest()

def followObject():
    rospy.init_node('follow_object')
    sub = rospy.Subscriber('raspicam_node/image/compressed', CompressedImage, callbackImage)
    

    rospy.spin()

if __name__ == '__main__':
    followObject()
