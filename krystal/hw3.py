# Name: Krystal Kwan
# Date: Tuesday, July 21, 2015
# Topic: Calculating the Perimeter and area of a rectangle and triangle

continuation = "y"

while continuation == "y":
    def triangle_area():
        print "You picked triangle, what is the base of the triangle(cm)?"
        b = raw_input("> ")
        print "What is the height of the triangle(cm)?"
        h = raw_input("> ")
        
    def rectangle_area():
        print "You picked rectangle, what is the width of the rectangle(cm)?"
        w = int(raw_input("> "))
        print "What is the length of the rectangle(cm)?"
        l = int(raw_input("> "))
        area_of_rect = w * l
        print "The area of the rectangle is %i" % (area_of_rect)
        

    print "Please pick a shape:"
    print "\t 1) rectangle"
    print "\t 2) triangle"

    shape = raw_input("> ")

    if shape == "rectangle" or shape == "1":
        rectangle_area()
    #elif shape == "triangle" or shape == "2":
        #triangle_area() 
    else:
        print "Invalid choice."


    print "Do you want to continue?"
    continuation = raw_input("> ")

        
