# Name: Krystal Kwan
# Date: 7/11/2015

from sys import argv

script_name, num_1, num_2 = argv
num_1 = int(num_1)
num_2 = int(num_2)

def max(largest_number):
    print largest_number


if num_1 > num_2:
    largest_number = num_1
    max(largest_number)
else:
    largest_number = num_2
    max(largest_number)
