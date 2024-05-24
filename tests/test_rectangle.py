def test_area(rectangle):
    assert rectangle.area() == 10 * 20


def test_perimeter(rectangle):
    res = rectangle.perimeter()
    assert res == 10 * 2 + 20 * 2


def test_not_equal(rectangle, another_rectangle):
    assert rectangle != another_rectangle
