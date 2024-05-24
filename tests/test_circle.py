import math
import src.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        print(f"settting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        res = self.circle.perimeter()
        assert res == math.pi * self.circle.radius
