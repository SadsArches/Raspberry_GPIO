import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

servo=11
GPIO.setup(servo,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(2.1)
time.sleep(3)
for i in range (0,180):
    DC=8.9/180.*(i)+2.1
    pwm.ChangeDutyCycle(DC)
    time.sleep(0.01)

pwm.stop()
GPIO.cleanup()
