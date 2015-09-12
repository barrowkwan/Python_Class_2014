#!usr/bin/env python
#Ian Wong
#9/5/15
#Printing
def letters(name,last):
    full = name + last
    return full

name=raw_input("What is your first name?")
last=raw_input("What is your last name?")
    
full_name = letters(name,last)

print "Your name is %s" % (full_name)
