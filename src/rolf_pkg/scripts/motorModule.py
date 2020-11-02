import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, In1, In2, En):
        self.In1 = In1
        self.In2 = In2
        self.En = En
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        GPIO.setup(self.En,GPIO.OUT)
        self.pwm = GPIO.PWM(self.En, 100)
        self.pwm.start(0)

    def move(self, speed=0.5):
        # scale normalized speed to value between -100 and 100
        speed *= 100
        speed = min(speed, 100)
        speed = max(speed, -100)

        self.pwm.ChangeDutyCycle(abs(speed))

        # forward
        if speed >= 0:
            GPIO.output(self.In1, GPIO.HIGH)
            GPIO.output(self.In2, GPIO.LOW)
        # backward
        else:
            GPIO.output(self.In1, GPIO.LOW)
            GPIO.output(self.In2, GPIO.HIGH)

    def stop(self):
        # stop motor
        self.pwm.ChangeDutyCycle(0)