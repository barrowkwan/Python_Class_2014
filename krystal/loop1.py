# Krystal Kwan
# python
# loops

print "Number?"
num = int(raw_input("> "))
num = num + 1

def count_up():
    global num
    for i in range(1, num, 1):
        print i

count_up(num)
