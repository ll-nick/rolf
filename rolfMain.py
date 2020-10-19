from rolf import Rolf
import keyPressModule as kp
import gamepadModule as gp
import RPi.GPIO as GPIO
from time import sleep

input = 'Gamepad' #['Keyboard','Gamepad']

rolf = Rolf()
kp.init()

def main():
    speed = 0
    turn = 0

    if input == 'Gamepad':
        gamepad = gp.getGamepad()
        if gamepad['R1']:
            speed = 0
            turn = 0
        else:
            speed = -gamepad['axis3']
            turn = -gamepad['axis0']
    else:
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

    rolf.move(speed, turn)

if __name__ == '__main__':
    while True:
        if kp.getKey('x'):
            print("Program Ended")
            rolf.stop()
            break
        main()

    GPIO.cleanup()