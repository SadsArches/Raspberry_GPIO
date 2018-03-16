import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

forward=11
backward=13
regulator=7

GPIO.setup(forward,GPIO.OUT)
GPIO.setup(backward,GPIO.OUT)
GPIO.setup(regulator,GPIO.OUT)

GPIO.output(forward,True)
GPIO.output(backward,False)
velocity= GPIO.PWM(regulator , 100)

velocity.start(0)

for x in range (0,10):
    V=input("set velocity of the motor (0%-100%)")
    if (V>=0 and V<=100):
        velocity.ChangeDutyCycle(V)

velocity.stop()
GPIO.output(forward,False)
GPIO.output(backward,False)
GPIO.cleanup()
