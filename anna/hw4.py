# Anna Lee
# July 19, 2015
# Max and Min

num_1 = int(raw_input("First number:"))
num_2 = int(raw_input("Second number:"))
num_3 = int(raw_input("Third number:"))
num_4 = int(raw_input("Fourth number:"))
num_5 = int(raw_input("Fifth number:"))

def max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def min(num_1, num_2):
    if num_1 < num_2:
        return num_1
    else:
        return num_2

print 'Max: %d' % max(max(max(max(num_1, num_2), num_3), num_4), num_5)
print 'Min: %d' % min(min(min(min(num_1, num_2), num_3), num_4), num_5)

