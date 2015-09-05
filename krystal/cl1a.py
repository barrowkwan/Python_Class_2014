#!/usr/bin/env python
#
# Name: Krystal Kwan
# Date: 9/5/2015
# Description: asks the name and tells you how many letters your name has

def letter_name():
    global name
    numbers = len(name)
    print "You have %i letters in your name." % (numbers)

print "What is your name?"
name = raw_input('> ')

letter_name()
