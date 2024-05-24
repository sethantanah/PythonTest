def add(num_one: int, num_two: int) -> int:
    return num_one + num_two


def devide(num_one: int, num_two: int) -> int:
    if num_two == 0:
        raise ValueError
    return num_one / num_two
