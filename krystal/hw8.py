# Name: Krystal Kwan
# Date: 1/17/2016
# Description: count how many word in this string
#!/usr/bin/env python

print "String: "
string = raw_input("> ")
c = 0
for i in string:
    if i == " ":
        c = c + 1
    else:
        continue
print "Amount of words: %i" % (c)
