#!/usr/bin/env python
#Name:Ian Wong
#Date:12/20/15
#Assignment:Python Counting Program
import sys
first = print (input("What is your first number"))
second  = print (input("What is your second number"))
def one():
	for i in range(first,second):
		print (i)

def two():
	for i in range(2,20,2):
		print (i)
def three():
	for i in range(21,0,-2):
		print (i)

one()
two()
three()
