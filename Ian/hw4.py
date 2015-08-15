#Ian Wong
#July 28,2015
#Maximum and Minimum
num1=int(raw_input("Number 1:"))
num2=int(raw_input("Number 2:"))
num3=int(raw_input("Number 3:"))
num4=int(raw_input("Number 4:"))
num5=int(raw_input("Number 5:"))

def max_num(x,y):
    if x > y:
        return x
    else:
        return y
ma=max(max(max(max(num1,num2),num3),num4),num5)
print "Maximum: %d" % ma

def min_num(x,y):
    if x < y:
        return x
    else:
        return y
mi=min(min(min(min(num1,num2),num3),num4),num5)
print "Minimum: %d" % mi
