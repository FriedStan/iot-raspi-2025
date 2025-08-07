import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
RED=5
GREEN=6
BLUE=13

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

while True:
 GPIO.output(RED,False)
 time.sleep(1)
 GPIO.output(GREEN,False)
 time.sleep(1)
 GPIO.output(GREEN,True)
 GPIO.output(BLUE,False)
 time.sleep(1)
 GPIO.output(RED,True)
 GPIO.output(GREEN,False)
 time.sleep(1)
 GPIO.output(BLUE,True)
 time.sleep(1)
 GPIO.output(GREEN,True)
 GPIO.output(BLUE,False)
 time.sleep(1)
 GPIO.output(GREEN,False)
 GPIO.output(RED,False)
 time.sleep(1)
 GPIO.output(GREEN,True)
 GPIO.output(BLUE,True)
