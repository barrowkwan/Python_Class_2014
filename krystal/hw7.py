# Name: Krystal Kwan
# Date: 1/17/2016
# Description: Stop printing string at dash. Do not print dash.
#!/usr/bin/env python

print "String: "
string = raw_input("> ")
dash = "-"
for i in string:
    if i == dash:
        break
    else:
        print i
