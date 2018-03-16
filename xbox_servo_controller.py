import time
import RPi.GPIO as GPIO
import xbox
GPIO.setmode(GPIO.BOARD)

joy = xbox.Joystick()
servo1=11
servo2=13
GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
pwm1=GPIO.PWM(servo1,50)
pwm2=GPIO.PWM(servo2,50)
pwm1.start(6)
pwm2.start(6)

print(joy.rightX())
while 1:
    j=(joy.rightX())
    i=90*(j+1)
    DC1=8.9/180.*(i)+2.1
    pwm1.ChangeDutyCycle(DC1)

    s=(joy.rightY())
    c=90*(s+1)
    DC2=8.9/180.*(c)+2.1
    pwm2.ChangeDutyCycle(DC2)
    

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
