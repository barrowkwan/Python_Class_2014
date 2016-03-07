#!usr/bin/env python
#Name: Anna Lee
#Date: January 17, 2016
#Description: Do not print dash

string = (raw_input("What is your string? Make sure you have a dash in your string."))

for i in string:
	if i == "-":
		break
	else:
		print i
