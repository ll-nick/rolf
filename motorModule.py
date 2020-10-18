import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

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
        # check requested direction
        forward = speed >= 0
        
        # scale normalized speed to value between -100 and 100
        speed *= 100
        speed = abs(speed)
        speed = min(speed, 100)

        # forward
        if forward:
            GPIO.output(self.In1, GPIO.High)
            GPIO.output(self.In2, GPIO.LOW)
        # backward
        else:
            GPIO.output(self.In1, GPIO.LOW)
            GPIO.output(self.In2, GPIO.High)
        
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        # stop motor
        self.pwm.ChangeDutyCycle(0)