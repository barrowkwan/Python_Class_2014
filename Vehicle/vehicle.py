# Krystal Kwan
# 9/3/2016
# Make a class

class Vehicle:
    def __init__(self, name, color, no_of_wheels, no_of_seats, no_of_windows, brand):
        self.name = name
        self.color = color
        self.no_of_wheels = no_of_wheels
        self.no_of_seats = no_of_seats
        self.no_of_windows = no_of_windows
        self.brand = brand
        self.x = 0
        self.y = 0
        self.heading = 1

    def displayColor(self):
        print("%s's vehicle's color is %s." % (self.name, self.color))

    def displayWheels(self):
        print("%s's vehicle's number of wheels is %s." % (self.name, self.no_of_wheels))

    def displaySeats(self):
        print("%s's vehicle's number of wheels is %s." % (self.name, self.no_of_seats))

    def displayWindows(self):
        print("%s's vehicle's number of wheels is %s." % (self.name, self.no_of_windows))

    def displayBrand(self):
        print("%s's vehicle's brand is %s." % (self.name, self.brand))

    def myPosition(self):
        print("%s is at %i,%i" % (self.name, self.x, self.y))

    def myPositions(self,x,y):
        self.x = x
        self.y = y

    def moveForward(self, steps):
        if self.heading == 1:
            self.y += steps
            return

        if self.heading == 2:
            self.x += steps
            return

        if self.heading == 3:
            self.y -= steps
            return

        if self.heading == 4:
            self.x -= steps
            return

    def moveBackward(self, steps):
        if self.heading == 1:
            self.y -= steps
            return
        if self.heading == 2:
            self.x -= steps
            return
        if self.heading == 3:
            self.y += steps
            return
        if self.heading == 4:
            self.x += steps
            return
    def moveForward(self,steps):
        if self.heading == 1:
            self.y += steps
            return
        if self.heading == 2:
            self.x += steps
            return
        if self.heading == 3:
            self.y -= steps
            return
        if self.heading == 4:
            self.x -= steps
            return

    def moveBackward(self, steps):
        if self.heading == 1:
            self.y -= steps
            return
        if self.heading == 2:
            self.x -= steps
            return
        if self.heading == 3:
            self.y += steps
            return
        if self.heading == 4:
            self.x += steps
            return

    def turnRight(self):
        self.heading += 1
        if self.heading >= 5:
            self.heading = 1

    def turnLeft(self):
        self.heading -= 1
        if self.heading <= 0:
            self.heading = 1
