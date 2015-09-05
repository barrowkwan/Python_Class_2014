#!usr/bin/env python
#Ian Wong
#9/5/15
#Printing

print str("hello world")
print 100
x = "Hello World"
y = 100
print "%s : %i" % (x,y)

a = "100"
b = "200"

print "Sum of a + b = %i" % (int(a)+int(b))

name=str(raw_input("What is your name?"))
born=int(raw_input("How old are you?"))
print "%s, you are %i years old." % (name,born)
print "10 years later you are %i years old" % (born+10)

from random import randint
i=randint(1,99)
j=randint(1,99)
print "%i + %i = %i" % (i,j,i+j)
