#!/usr/bin/env python
#Name: Ian Wong
#Date: 1/3/16
#Assignment: Counting Vowels

string = input("What is your string?")

string = string.lower()
count1= string.count('a')
count2 = string.count('e')
count3 = string.count('i')
count4 = string.count('o')
count5 = string.count('u')

print ("There are %i a in the text." % (count1))
print ("There are %i e in the text." % (count2))
print ("There are %i i in the text." % (count3))
print ("There are %i o in the text." % (count4))
print ("There are %i u in the text." % (count5))

