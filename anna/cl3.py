#Anna Lee
#9/12/15
#write function that takes one arguement as a number then will square the number and return it

def square(n):
    n = n*n
    return n

def string(s):
    s = s[:2] + s[3:]
    return s

n = int(raw_input('What is your lucky number?'))
s = raw_input('What is your word?')

p = square(n)
print 'Your number squared is %i.' % p

w = string(s)
print 'Your new word is %s' % w

#PASS STRING TO FUNCTION THEN REMOVE THE SECOND LETTER IN THE STRING THEN RETURN THE STRING 
