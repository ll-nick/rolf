#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import keyPressModule as kp

def readKeyboard():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('keyboard_getter', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    kp.init()

    while not rospy.is_shutdown():
        forward = kp.getKey('UP')
        backward = kp.getKey('DOWN')
        left = kp.getKey('LEFT')
        right = kp.getKey('RIGHT')
        stop = kp.getKey('SPACE')

	if stop:
	    speed = 0
            turn = 0
	else:
	    if forward and not backward:
                speed = 1
            elif not forward and backward:
                speed = -1
            else:
                speed = 0

            if left and not right:
                turn = 1
            elif not left and right:
                turn = -1
            else:
                turn = 0
        
        outstr = "Speed: " + speed + ", Turn: " + turn
        pub.publish(outstr)
        rate.sleep()

if __name__ == '__main__':
    try:
        readKeyboard()
    except rospy.ROSInterruptException:
        pass
