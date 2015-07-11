# Anna Lee
# July 11, 2015
# Max

from sys import argv

num_1 = int(raw_input("First number:"))
num_2 = int(raw_input("Second number:"))

def max(num_1, num_2):
    if num_1 > num_2:
        print num_1
        return num_1
    else:
        print num_2
        return num_2

max(num_1, num_2)

