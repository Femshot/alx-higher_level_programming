#!/usr/bin/python3
"""Module containing a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class

    Or if the object is an instance of a class that inherited from
    the specified class

    Args:
        obj: Object as first argument
        a_class: Class to check object against

    Return:
        True: if exactly same instance
        False: if notexactly same instance
    """
    if isinstance(obj, a_class):
        return True
    return False
