#Ian Wong
#7/11/15 : Question 2,max

num1=int(raw_input("Number 1:"))
num2=int(raw_input("Number 2:"))
num3=int(raw_input("Number 3:"))

def max_of_three(num1,num3,num2):
    if num1 >num2 and num3:
        return num1
    if num2 >num1 and num3:
        return num2
    else:
        return num3

max_of_three(num1,num2,num3)
