import RPi.GPIO as GPIO
import xbox
import time

GPIO.setmode(GPIO.BOARD)
joy = xbox.Joystick()

forward=11
backward=13
regulator=7

GPIO.setup(forward,GPIO.OUT)
GPIO.setup(backward,GPIO.OUT)
GPIO.setup(regulator,GPIO.OUT)

GPIO.output(forward,True)
GPIO.output(backward,False)
velocity= GPIO.PWM(regulator , 1000)

velocity.start(0)
delay=0.01
while not joy.Back():
    time.sleep(delay)
    if not joy.B():
        b=(joy.rightTrigger())*50
    else:
        b=(joy.rightTrigger())*100
    print b
    velocity.ChangeDutyCycle(b)
    if not joy.Y():
        GPIO.output(forward,True)
        GPIO.output(backward,False)
    else:
        GPIO.output(forward,False)
        GPIO.output(backward,True)
    
joy.close()
velocity.stop()
GPIO.output(forward,False)
GPIO.output(backward,False)
GPIO.cleanup()
