import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

class Motor():
    def __init__(self, In1, In2):
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwmA = GPIO.PWM(self.In1, 100)
        self.pwmB = GPIO.PWM(self.In2, 100)
        self.pwmA.start(0)
        self.pwmB.start(0)

    def move(self, speed=0.5, t=0):
        # scale normalized speed to value between -100 and 100
        speed *= 100
        speed = max(speed, -100)
        speed = min(speed, 100)

        # forward
        if speed >= 0:
            self.pwmA.ChangeDutyCycle(speed)
            GPIO.output(self.In2, GPIO.LOW)
        # backward
        else:
            self.pwmB.ChangeDutyCycle(speed)
            GPIO.output(self.In1, GPIO.LOW)
                
        sleep(t)

    def stop(self, t=0):
        # stop motor
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)

        sleep(t)