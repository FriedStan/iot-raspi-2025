import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LIGHT=4
BUTTON=17

GPIO.setup(LIGHT,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN)

while True:
 val=GPIO.input(BUTTON)
 if val==1:
  GPIO.output(LIGHT,False)
 else:
  GPIO.output(LIGHT,True)
