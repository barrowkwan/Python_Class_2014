#!/user/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def flash():
  GPIO.output(13, False)
  for i in range(5):
    GPIO.output(5, True)
    time.sleep(1)
    GPIO.output(5, False)
    time.sleep(1)
  GPIO.output(24, True)

while True:
  GPIO.output(24, True)
  GPIO.output(5, True)
  GPIO.output(25, False)
  GPIO.output(16, False)
  GPIO.output(13, False)  
  if(GPIO.input(12) == 0):
    GPIO.output(16,True) 
    GPIO.output(24, False)
    time.sleep(2)
    GPIO.output(13, True)
    GPIO.output(25, True)
    GPIO.output(16, False)
    GPIO.output(5, False)
    time.sleep(5)
    flash()    
  if(GPIO.input(12) == 1):
    GPIO.output(24,False)


