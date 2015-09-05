#!/usr/bin/env python
#
# Name: Krystal Kwan
# Date: 9/5/2015
# Description: generates 2 random numbers and gives the sum of both of them

from random import *

a = randint(1,99)
b = randint(1,99)
c = a + b

print "The sum of %i + %i = %i." % (a, b, c)
