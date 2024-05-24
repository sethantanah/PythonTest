import pytest
import src.shapes as shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(20, 10)
