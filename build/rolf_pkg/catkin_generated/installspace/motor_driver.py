#!/usr/bin/env python2
import rospy
from rolf_pkg.msg import ControlRequest
from rolf import Rolf

def callbackControlRequest(msg):
    rolf.move(msg.speed, msg.turn)

def motorDriver():
    rospy.init_node('motor_driver', anonymous=True)
    rospy.Subscriber("rolf/control_request", ControlRequest, callbackControlRequest)

    rolf = Rolf()

    rospy.spin()

if __name__ == '__main__':
    motorDriver()
