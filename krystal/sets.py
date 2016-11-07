# Krystal Kwan
# 11/6/2016

my_list = [49, 66, 43, 49, 22, 89, 49, 33, 22, 66, 49, 55]
num_items_in_list = len(my_list)
my_numlist = {}
my_numlist[49] = 0
for i in my_list:
    print (i)
    my_numlist[i] += 1
print ("\n")
print (num_items_in_list)
print (my_list.count("49"))