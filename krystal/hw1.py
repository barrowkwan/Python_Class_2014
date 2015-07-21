# Name: Krystal Kwan
# Date: Monday, July 20, 2015
# Topic: Maxium and Minimum

from sys import argv

script, num1, num2, num3, num4, num5 = argv

def find_the_max_number(num1, num2, num3, num4, num5):
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        print "Maximum number: %i" % (num1)

    elif num2 > num3 and num2 > num4 and num2 > num5 and num2 > num1:
        print "Maximum number: %i" % (num2)

    elif num3 > num4 and num3 > num5 and num3 > num1 and num3 > num2:
        print "Maximum number: %i" % (num3)

    elif num4 > num5 and num4 > num1 and num4 > num2 and num4 > num3:
        print "Maximum number: %i" % (num4)

    else:
        print "Maximum number: %i" % (num5)

def find_the_min_number(num1, num2, num3, num4, num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        print "Minimum number: %i" % (num1)

    if num2 < num3 and num2 < num4 and num2 < num5 and num2 < num1:
        print "Minimum number: %i" % (num2)

    if num3 < num4 and num3 < num5 and num3 < num1 and num3 < num2:
        print "Minimum number: %i" % (num3)

    if num4 < num5 and num4 < num1 and num4 < num2 and num4 < num3:
        print "Minimum number: %i" % (num4)

    else:
        print "Minimum number: %i" % (num5)
num1 = int(num1)

num2 = int(num2)

num3 = int(num3)

num4 = int(num4)

num5 = int(num5)

find_the_max_number(num1, num2, num3, num4, num5)
find_the_min_number(num1, num2, num3, num4, num5)
