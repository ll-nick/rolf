#!/usr/bin/env python

import rospy
from rolf_pkg.msg import ControlRequest
import gamepadModule as gp

def readGamepad():
    pub = rospy.Publisher('rolf/control_request', ControlRequest, queue_size=10)
    rospy.init_node('gamepad_getter', anonymous=True)
    rate = rospy.Rate(100)
    msg = ControlRequest()
    while not rospy.is_shutdown():
        if gp.getStop():
            speed = 0
            turn = 0
        else:
            speed = gp.getSpeed()
            turn = gp.getTurn()

        msg.header.stamp = rospy.Time.now()
        msg.speed = speed
        msg.turn = turn
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        readGamepad()
    except rospy.ROSInterruptException:
        pass
