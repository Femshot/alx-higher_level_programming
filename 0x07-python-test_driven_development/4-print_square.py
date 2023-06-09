#!/usr/bin/python3
"""Module containing a function print_square"""


def print_square(size):
    """Prints out a square with the # character

    Args:
        size (int): Determines the size of the square

    Raises:
        TypeError: If size not int or float or if float but less than 0
        ValueError: if size int but less than 0
   """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0.0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print("")
    else:
        for i in range(size):
            print("#" * size)
