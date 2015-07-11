# Name: Krystal Kwan
# Date: 7/11/2015
# Description: define a function 'max()' that takes 3 numbers as argumuments

from sys import argv

script_name, num_1, num_2, num_3 = argv
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

def max_of_three(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_1 < num_2 and num_2 > num_3:
        return num_2
    else:
        return num_3

max_of_three(num_1, num_2, num_3)
