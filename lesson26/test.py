# __add__ +
# a + b -> a.__add__(b)

# __new__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} - {self.y}'

point = Point(3, 4)
print(point)

a = 1
print(str(point))
print(repr(point))
