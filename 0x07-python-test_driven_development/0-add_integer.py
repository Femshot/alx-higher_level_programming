#!/usr/bin/python3
"""Module contains a function add"""


def add_integer(a, b=98):
    """Adds two integers of floats together

    Args:
        a (int, float): First argument taken
        b (int, float): Second argument taken

    Raises:
        TypeError: if a or b not in integer or float

    Returns:
        Addition of both arguments
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise TypeError("a must be an integer")
    if b + 1 == b:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
