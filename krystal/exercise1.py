# Name: Krystal Kwan
# Date: 7/11/2015
# Description: define a function 'max()' that takes two numbers as argum

from sys import argv

script_name, num_1, num_2 = argv
num_1 = int(num_1)
num_2 = int(num_2)

def max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2
max(num_1, num_2)
