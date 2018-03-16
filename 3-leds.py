import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

red=15
green=13
blue=11

GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
s=0.5
for x in range (0,3):

    GPIO.output(red,True)
    time.sleep(s)
    GPIO.output(red,False)

    GPIO.output(green,True)
    time.sleep(s)
    GPIO.output(green,False)

    GPIO.output(blue,True)
    time.sleep(s)
    GPIO.output(blue,False)

    GPIO.output(green,True)
    time.sleep(s)
    GPIO.output(green,False)

for x in range (0,3):
    
    GPIO.output(red,True)
    time.sleep(s)
    GPIO.output(green,True)
    time.sleep(s)
    GPIO.output(blue,True)
    time.sleep(s)

    GPIO.output(red,False)
    time.sleep(s)
    GPIO.output(green,False)
    time.sleep(s)
    GPIO.output(blue,False)
    time.sleep(s)


GPIO.cleanup()
