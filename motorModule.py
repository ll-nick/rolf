import RPi.GPIO as GPIO
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

    def move(self, speed=0.5):
        forward = speed >= 0
        # scale normalized speed to value between -100 and 100
        speed *= 100
        speed = abs(speed)
        speed = min(speed, 100)

        # forward
        if forward:
            self.pwmA.ChangeDutyCycle(speed)
            GPIO.output(self.In2, GPIO.LOW)
        # backward
        else:
            self.pwmB.ChangeDutyCycle(speed)
            GPIO.output(self.In1, GPIO.LOW)

    def stop(self):
        # stop motor
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)