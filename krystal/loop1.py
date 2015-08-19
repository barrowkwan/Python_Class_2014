# Krystal Kwan
# python
# loops

def count_up():
    global num
    for i in range(1, num, 1):
        print i

print "Number?"
num = int(raw_input("> "))
num = num + 1

count_up(num)
