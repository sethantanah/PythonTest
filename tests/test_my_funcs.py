import pytest
import time
import src.my_functions as my_functions


def test_add():
    res = my_functions.add(num_one=1, num_two=4)
    assert res == 5


def test_devide():
    res = my_functions.devide(num_one=10, num_two=2)
    assert res == 5


def test_devide_by_zero():
    with pytest.raises(ValueError):
        my_functions.devide(num_one=10, num_two=0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    res = my_functions.add(num_one=1, num_two=4)
    assert res == 5


@pytest.mark.skip(reason='This feature is broken')
def test_add_num():
    assert my_functions.add(num_one=1, num_two=4) == 5
