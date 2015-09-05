#!/usr/bin/env python
#
# Name: Krystal Kwan
# Date: 9/5/2015
# Description: asks the name and tells you how many letters your name has

def letter_name(name):
    numbers = len(name)
    return int(numbers)

print "What is your name?"
name = raw_input('> ')
numbers = 0

letter_name(name)
print "Your name has %s letters." % (letter_name(name))
