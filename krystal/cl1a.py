#!/usr/bin/env python
#
# Name: Krystal Kwan
# Date: 9/5/2015
# Description: asks the name and tells you how many letters your name has (only 5 lines of coding!)

def full_name(first, last):
    return (first + " " + last)

first = raw_input("What is your first name? ")
last = raw_input("What is your last name? ")

print "%s" % (full_name(first, last))
