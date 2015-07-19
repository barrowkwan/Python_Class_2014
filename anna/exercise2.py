# Anna Lee
# July 11, 2015
# Max

from sys import argv

num_1 = int(raw_input("First number:"))
num_2 = int(raw_input("Second number:"))
num_3 = int(raw_input("Third number:"))

def max_of_three(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        print num_1
        return num_1
    elif num_2 > num_1 and num_2 > num_3:
        print num_2
        return num_2
    else:
        print num_3
        return num_3

max_of_three(num_1, num_2, num_3)

