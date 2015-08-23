# Name: Krystal Kwan
# Date: Monday, July 20, 2015
# Topic: Maxium and Minimum

from sys import argv

script, num1, num2, num3, num4, num5 = argv

num1 = int(num1)

num2 = int(num2)

num3 = int(num3)

num4 = int(num4)

num5 = int(num5)

def max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def min(num_1, num_2):
    if num_1 < num_2:
        return num_1
    else:
        return num_2

print "Max: %i" % max(max(max(max(num1, num2), num3), num4), num5)
print "Min: %i" % min(min(min(min(num1, num2), num3), num4), num5)
