import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led=7

GPIO.setup(led,GPIO.OUT)
p = GPIO.PWM(led , 200)
p.start(0)
while (1):
    for x in range(0,100):
        p.ChangeDutyCycle(x)
        time.sleep(0.01)

    for x in range(0,100):
        p.ChangeDutyCycle((x-100)*-1)
        time.sleep(0.01)

p.stop()
GPIO.cleanup()
