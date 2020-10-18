from motorModule import Motor
from time import sleep

class Rolf():
    def __init__(self):
        self.fr = Motor(0,1)
        self.rr = Motor(5,6)
        self.fl = Motor(10,9)
        self.rl = Motor(8,7)

    def move(self, speed=0.5, turn=0, t=0):
        leftSpeed = speed - turn
        rightSpeed = speed + turn

        self.fl.move(leftSpeed)
        self.rl.move(leftSpeed)
        self.fr.move(rightSpeed)
        self.rr.move(rightSpeed)
        sleep(t)

    def stop(self, t=0):
        self.fl.stop()
        self.rl.stop()
        self.fr.stop()
        self.rr.stop()
        sleep(t)