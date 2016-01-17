#Ian Wong
#July 28,2015
#Maximum and Minimum

num1=int(raw_input("Number 1:"))
num2=int(raw_input("Number 2:"))
num3=int(raw_input("Number 3:"))
num4=int(raw_input("Number 4:"))
num5=int(raw_input("Number 5:"))

def max_num(num1,num2,num3,num4,num5,):
    if num1 > num2 and num1 > num3 and num1> num4 and num1 > num5:
        print "Maximum Number:%d" % num1
    elif num2 > num1  and num2 > num3 and num2 > num4 and num2 > num5:
        print "Maximum Number:%d" % num2
    elif num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5:
        print "Maximum Number:%d" % num3
    elif num4 > num2  and num4 > num3 and num4 > num1 and num4 > num5:
        print "Maximum Number:%d" % num4
    else:
        print "Maximum Number:%d" % num5
    
def min_num(num1,num2,num3,num4,num5,):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        print "Minimum Number:%d" % num1
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        print "Minimum Number:%d" % num2
    elif num3 < num2 and num3 < num1 and num3 < num4 and num3 < num5:
        print "Minimum Number:%d" % num3
    elif num4 < num2 and num4 < num3 and num4 < num1 and num4 < num5:
        print "Minimum Number:%d" % num4
    else:
        print "Minimum Number:%d" % num5

max_num(num1,num2,num3,num4,num5,)
min_num(num1,num2,num3,num4,num5,)
   
 
