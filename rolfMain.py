from rolf import Rolf
import keyPressModule as kp
import RPi.GPIO as GPIO

rolf = Rolf()
kp.init()

#rolf.move(0, 1, 1)
#rolf.stop()

def main():
    #print(kp.getKey('Left'))
    forward = kp.getKey('UP')
    backward = kp.getKey('DOWN')
    left = kp.getKey('LEFT')
    right = kp.getKey('RIGHT')
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

    rolf.move(speed, turn, 0.1)

if __name__ == '__main__':
    while True:
        if kp.getKey('x'):
            print("Program Ended")
            rolf.stop()
            break
        main()

    GPIO.cleanup()