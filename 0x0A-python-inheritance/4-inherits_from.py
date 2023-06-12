#!/usr/bin/python3
"""Module containin a function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object asfirst argument.
        a_class: The class to check against.

    Returns:
        True: If obj is an inherited instance of a_class
        False: If obj is not an inherited(derived) instance or if of same type
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
