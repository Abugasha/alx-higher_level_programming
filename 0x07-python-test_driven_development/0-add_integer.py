#!/usr/bin/python3
"""
add_integer returns the sum of two integers
c = a + b
gives back a c
"""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a: first number.
        b: second number.

    Returns:
        return a + b.

    Raises:
        TypeError: if a or b is not float
        or is not int
        cant multiply.
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if (type(a) is not int):
        raise TypeError("a must be an integer")
    if (type(b) is not int):
        raise TypeError("b must be an integer")
    return (a + b)
