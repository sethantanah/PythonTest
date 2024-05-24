import math


class Shape:
    def area():
        pass

    def perimeter():
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return self.length * 2 + self.width * 2

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False

        if self.width == other.width and self.length == other.length:
            return True
        else:
            return False


class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)
