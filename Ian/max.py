#Ian Wong
#7/11/15 : Question 1,max
#from sys import argv
#num1, num2 =argv

num1=(raw_input("Number 1:"))
num2=(raw_input("Number 2:"))

def max(num1,num2):
    if num1>num2:
        print num1
        return num1
    if num2>num1:
        print num2
        return num2

max(num1,num2)
