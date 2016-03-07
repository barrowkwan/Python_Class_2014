# Krystal Kwan
# 2/14/2016
# Make questions for a first grader
#!/usr/bin/env python

from random import randint
s = 0
for i in range(1,11):
    num1 = randint(1,99)
    num2 = randint(1,99)
    print "%i. %i + %i = " % (i, num1, num2)
    ans = int(raw_input("> "))
    if ans == num1 + num2:
        s += 1
print "You have %i out of 10 questions correct." % (s)
