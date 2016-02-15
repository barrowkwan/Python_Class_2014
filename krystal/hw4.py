# Name: Krystal Kwan
# Date: Monday, July 20, 2015
# Topic: Maximum and Minimum

from sys import argv

script, num1, num2, num3, num4, num5, num6 = argv

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2




num1 = int(num1)

num2 = int(num2)

num3 = int(num3)

num4 = int(num4)

num5 = int(num5)

num6 = int(num6)

print "Max: %i" % max(max(max(max(num1, num2), num3), num4), num5)
