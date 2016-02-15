#!/usr/bin/python
#
# Name : Barrow Kwan
# Date : 7/11/2015
# Description : Program to find the maximum number
#
#

import sys


def max(num1,num2):
  if num1 > num2:
    return num1
  else:
    return num2


print "The largest number is %d." %  max(int(sys.argv[1]),int(sys.argv[2]))

