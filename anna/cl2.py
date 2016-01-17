age = 10

def my_age():
    global age
    age = 20
    print 'my age :%i' % age

my_age()
print 'age:%i' % age

