#!/user/bin/env python
#Name: Anna Lee
#Date: December 20, 2015
#Description: Counting
import sys

f = int(input("What is your first number?"))
s = int(input("What is your second number?"))

def one(f,s):
  for i in range (f,s):
    print (i)

def two():
  for i in range (2, 21, 2):
    print (i)

def three():
  for i in range (20, 1, -2):
    print (i)

one(f,s)
two()
three()

