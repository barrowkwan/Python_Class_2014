#!usr/bin/env/python
#Name: Ian Wong
#Date: 1/17/16
#Assignment: Printing String

string = raw_input(str("What is your string?"))

count = string.count("-")

for i in string:
	if i == "-":
		break
	else:
		print i
