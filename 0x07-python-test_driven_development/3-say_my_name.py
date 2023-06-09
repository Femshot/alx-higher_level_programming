#!/usr/bin/python3
"""Module containing a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Prints a full name

    Args:
        first_name (str): First Argument
        last_name (str): second Argument

    Raises:
        TypeError: Exception if arguments aren't string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
