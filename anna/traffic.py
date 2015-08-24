# Name: Krystal, Anna, Ian
# Date: 8/24/2015 
# Description: Traffic and Pedestrian Lights with LCD
#!/user/bin/env python

import RPi.GPIO as GPIO
import time
import lcddriver

lcd = lcddriver.lcd()
lcd.lcd_clear();

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
  GPIO.output(5, True)
  lcd.lcd_display_string("To Cross 5",2)
  time.sleep(0.5)
  GPIO.output(5, False)
  time.sleep(0.5)
  GPIO.output(5, True)
  lcd.lcd_display_string("To Cross 4",2)
  time.sleep(0.5)
  GPIO.output(5, False)
  time.sleep(0.5)
  GPIO.output(5, True)
  lcd.lcd_display_string("To Cross 3",2)
  time.sleep(0.5) 
  GPIO.output(5,False)
  time.sleep(0.5)
  GPIO.output(5, True)
  lcd.lcd_display_string("To Cross 2",2)
  time.sleep(0.5)
  GPIO.output(5, False)
  time.sleep(0.5)
  GPIO.output(5, True)
  lcd.lcd_display_string("To Cross 1",2)
  time.sleep(0.5)

while True:
  GPIO.output(24, True)
  GPIO.output(5, True)
  lcd.lcd_display_string("Do Not",1)
  lcd.lcd_display_string("Cross",2)
  GPIO.output(25, False)
  GPIO.output(16, False)
  GPIO.output(13, False)  
  if(GPIO.input(12) == 0):
    GPIO.output(16,True) 
    GPIO.output(24, False)
    time.sleep(2)
    GPIO.output(13, True)
    lcd.lcd_clear();
    lcd.lcd_display_string("You Are Allowed", 1)
    lcd.lcd_display_string("To Cross", 2)
    GPIO.output(25, True)
    GPIO.output(16, False)
    GPIO.output(5, False)
    time.sleep(5)
    flash()    
    lcd.lcd_clear();
  if(GPIO.input(12) == 1):
    GPIO.output(24,False)


