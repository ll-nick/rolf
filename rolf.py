from motorModule import Motor

class Rolf():
    def __init__():
        fr = Motor(0,1)
        rr = Motor(5,6)
        fl = Motor(10,9)
        rl = Motor(8,7)

    def move(self, speed=0.5, turn=0, t=0):
        leftSpeed = speed - turn
        rightSpeed = speed + turn

        self.fl.move(leftSpeed, t)
        self.rl.move(leftSpeed, t)
        self.fr.move(rightSpeed, t)
        self.rr.move(rightSpeed, t)

    def stop(self, t=0):
        self.fl.stop(t)
        self.rl.stop(t)
        self.fr.stop(t)
        self.rr.stop(t)