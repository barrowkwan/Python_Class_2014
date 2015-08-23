#!/user/bin/env python

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)

while True:
  if(GPIO.input(23) ==0): 
    GPIO.output(4,True)
  if(GPIO.input(23) ==1):
    GPIO.output(4,False)
