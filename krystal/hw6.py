#Name: Krystal Kwan
# Date: 1/17/2016
# Description: Count how many vowels in each string
#!/usr/bin/env python

print "String: "
string = raw_input("> ")
vowels = "aeiou"
vowel1 = vowels.lower()
c = 0
for i in string:
    for j in vowels:
        if i == j:
            c = c + 1
        else:
            continue
print "Amount of vowels: %i" % (c)
