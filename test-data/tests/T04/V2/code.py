def cout_number(value):
    # Approximate C++ defaultfloat output: six significant digits.
    return format(value, ".6g")


class Shape:
    def area(self):
        raise NotImplementedError

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
    def __init__(self, side):
        super().__init__(side, side)

    def name(self):
        return "Square"


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return 3.14 * self.r * self.r

    def name(self):
        return "Circle"


shapes = [Rectangle(3, 4), Square(5), Circle(2)]

total = 0.0
for shape in shapes:
    area = shape.area()
    print(f"{shape.name()} area = {cout_number(area)}")
    total += area

print(f"Total area = {cout_number(total)}")
