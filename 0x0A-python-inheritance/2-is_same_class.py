#!/usr/bin/python3
"""Module containing a function is_same_class"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly the same instance of a class

    Args:
        obj: Object as first argument
        a_class: Class to check object against

    Return:
        True: if exactly same instance
        False: if notexactly same instance
    """
    if type(obj) is a_class:
        return True
    else:
        return False
