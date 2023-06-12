#!/usr/bin/python3
"""Module containing a class MyList"""


class MyList(list):
    """Class that  inherits the class list

    Args:
        list (class): A parent class
    """

    def print_sorted(self):
        """Prints out a ascending sorted list of object list instance"""
        print(sorted(self))
