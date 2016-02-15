# Anna Lee
# July 19, 2015
# Max and Min

num_1 = int(raw_input("First number:"))
num_2 = int(raw_input("Second number:"))
num_3 = int(raw_input("Third number:"))
num_4 = int(raw_input("Fourth number:"))
num_5 = int(raw_input("Fifth number:"))

def max(num_1, num_2, num_3, num_4, num_5):
    if num_1 > num_2 and num_1 > num_3 and num_1 > num_4 and num_1 > num_5:
        print "Maximum : %d" % num_1
        return num_1        
    elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4 and num_2 > num_5:
        print "Maximum : %d" % num_2
        return num_2
    elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4 and num_3 > num_5:
        print "Maximum : %d" % num_3
        return num_3
    elif num_4 > num_1 and num_4 > num_2 and num_4 > num_3 and num_4 > num_5:
        print "Maximum : %d" % num_4
        return num_4
    else:
        print "Maximum : %d" % num_5
        return num_5

:
        print "Maximum : %d" % num_1
        return num_1

def min(num_1, num_2, num_3, num_4, num_5):
    if num_1 < num_2 and num_1 < num_3 and num_1 < num_4 and num_1 < num_5:
    print "Minimum : %d" % num_1
        return num_1
    elif num_2 < num_1 and num_2 < num_3 and num_2 < num_4 and num_2 < num_5:
        print "Minimum : %d" % num_2
        return num_2
    elif num_3 < num_1 and num_3 < num_2 and num_3 < num_4 and num_3 < num_5:
        print "Minimum : %d" % num_3
        return num_3
    elif num_4 < num_1 and num_4 < num_2 and num_4 < num_3 and num_4 < num_5:
        print "Minimum : %d" % num_4
        return num_4
    else:
        print "Minimum : %d" % num_5
        return num_5

max(num_1, num_2, num_3, num_4, num_5)
min(num_1, num_2, num_3, num_4, num_5)
