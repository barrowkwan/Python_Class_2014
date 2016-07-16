# Name: Krystal Kwan
# Date: Tuesday, July 21, 2015
# Topic: Reversing Strings

print ("Input string")
string = input("> ")

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse(string)
iter(rev)

print ("Output string: %s" % (rev))

