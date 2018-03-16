import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

servo1=40
blue=7
GPIO.setup(servo1,GPIO.OUT)
pwm1=GPIO.PWM(servo1,50)
pwm1.start(2.1)

s=0.005

for l in range (0,30):

    j=180
    g=0
    for i in range (0,4):

        position=g
        DC1=8.9/180.*(position)+2.1
        pwm1.ChangeDutyCycle(DC1)
        g=g+45
        time.sleep(0.5)
    
    for i in range (0,180):
    
        position=j
        DC1=8.9/180.*(position)+2.1
        pwm1.ChangeDutyCycle(DC1)
        time.sleep(s)
        j=j-1

pwm1.stop()
GPIO.cleanup()
