class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def name(self):
        return "Shape"


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def name(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def name(self):
        return "Square"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def name(self):
        return "Circle"


# Polymorphism: different objects accessed through Shape interface
shapes = [
    Rectangle(3, 4),
    Square(5),
    Circle(2)
]

total = 0

for s in shapes:
    print(s.name(), "area =", s.area())
    total += s.area()

print("Total area =", total)
