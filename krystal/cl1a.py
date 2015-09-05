#!/usr/bin/env python
#
# Name: Krystal Kwan
# Date: 9/5/2015
# Description: asks the name and the age of the person

name = raw_input("Name: ")
age = int(raw_input("Age: "))
years = age + 10

print "Your name is %s and you are %i years old." % (name, age)
print "Ten years later, you will be %i years old." % (years)
