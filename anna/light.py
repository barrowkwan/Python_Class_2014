#! usr/bin/env python
#Name : Anna Lee
#Date : Jan. 31, 2016
#Description : Lights

import RPi.GPIO as GPIO 
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(18, False)
GPIO.output(24, False)
GPIO.output(25, False)

while 1 == 1:
  GPIO.output (18, True)
  sleep(0.05)
  GPIO.output(18, False)
  sleep(0.05)
  GPIO.output(24, True)
  sleep(0.05)
  GPIO.output(24, False)
  sleep(0.05)
  GPIO.output(25, True)
  sleep(0.05)
  GPIO.output(25, True)
  sleep(0.05)
  GPIO.output(25, False)
  sleep(0.05)
