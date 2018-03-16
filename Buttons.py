from time import sleep
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while (1):
    if GPIO.input(button1)==0:
        print "button 1 was pressed:"
        sleep(.2)
    if GPIO.input(button2)==0:
        print "button 2 was pressed:"
        sleep(.2)

