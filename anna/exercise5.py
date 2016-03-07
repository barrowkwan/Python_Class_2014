# Anna Lee
# July 19, 2015
# Area of Triangle and

choice = 0

def t_area(b, h):
    b = int(raw_input('Base: '))
    h = int(raw_input('Height: '))
    print 'The area of the triangle is %d' % (int(b * h / 2))
        
def r_area(l, w):
    l = int(raw_input('Legnth: '))
    w = int(raw_input('Width: '))
    print 'The area of the rectangle is %d' % (int(l * w))

def options():
    print 'Choose a shape'
    print '\t triangle'
    print '\t rectangle'
    #shape = raw_input

while choice == 0:
    shape = options()
    #shape = raw_input
    if shape == 'triangle':
        t_area(b, h)
    elif shape == 'rectangle':
        r_area(l, w)
    else:
        print 'That is not a choice'
           

    print 'Do you want to continue (y/n)?'
    yn = raw_input
    if yn == 'y':
        continue
    if yn == 'n':
        break  












