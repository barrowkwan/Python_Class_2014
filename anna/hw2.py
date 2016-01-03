#!usr/bin/env python
#Name: Anna Lee
#Date: Jan. 3, 2015
#Description: Count how many vowels

string = (input("What is your string?"))
s = string.lower()

a = s.count("a")
e = s.count("e")
i = s.count("i")
o = s.count("o")
u = s.count("u")
t = a + e + i + o + u

print ("There are %i As" % a)
print ("There are %i Es" % e)
print ("There are %i Is" % i)
print ("There are %i Os" % o)
print ("There are %i Us" % u)
print ("There are %i vowels in total" % t)
