# Name: Anna, Krystal
# Date: 8/24/2015
# Description: Nightlight Stimulator with 8 LEDs
#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier versions are not fast enough

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def RCtime (RCpin):
  reading = 0
  GPIO.setup(RCpin, GPIO.OUT)
  GPIO.output(RCpin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(RCpin, GPIO.IN)
  # This takes about 1 millisecond per loop cycle
  while (GPIO.input(RCpin) == GPIO.LOW):
    reading += 1
    if reading <= 20:
      GPIO.output(25, True) 
      GPIO.output(12, False)
      GPIO.output(16, False)
      GPIO.output(24, False)
      GPIO.output(23, False)
      GPIO.output(22, False)
      GPIO.output(17, False)
      GPIO.output(4, False)
    elif reading <= 40:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, False)
      GPIO.output(24, False)
      GPIO.output(23, False)
      GPIO.output(22, False)
      GPIO.output(17, False)
      GPIO.output(4, False)
    elif reading <= 60:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, True)
      GPIO.output(24, False)
      GPIO.output(23, False)
      GPIO.output(22, False)
      GPIO.output(17, False)
      GPIO.output(4, False)
    elif reading <= 80:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, True)
      GPIO.output(24, True)
      GPIO.output(23, False) 
      GPIO.output(22, False)
      GPIO.output(17, False)
      GPIO.output(4, False)
    elif reading <= 100:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, True)
      GPIO.output(24, True)
      GPIO.output(23, True)
      GPIO.output(22, False)
      GPIO.output(17, False)
      GPIO.output(4, False)
    elif reading <= 120:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, True)
      GPIO.output(24, True)
      GPIO.output(23, True)
      GPIO.output(22, True)
      GPIO.output(17, False)
      GPIO.output(4, False) 
    elif reading <= 140:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, True)
      GPIO.output(24, True)
      GPIO.output(23, True)
      GPIO.output(22, True)
      GPIO.output(17, True)
      GPIO.output(4, False)
    else:
      GPIO.output(25, True)
      GPIO.output(12, True)
      GPIO.output(16, True)
      GPIO.output(24, True)
      GPIO.output(23, True)
      GPIO.output(22, True)
      GPIO.output(17, True)
      GPIO.output(4, True)
  return reading

while True:
  print RCtime(18)  
  # Read RC timing using pin #18

