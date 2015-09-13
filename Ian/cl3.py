#write function take somethin return number squared
def squared(num):
    number = num * num
    return number

num =int(raw_input("What is your number?"))

new = squared(num)
print "The squared number is: %i" % new

def string(s):
    new = s[:3] + s[4:]
    return new
s = str(raw_input("What is your word?"))
word = string(s)
print "The new word is %s" % word
    
    
