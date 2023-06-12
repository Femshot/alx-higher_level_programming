#!/usr/bin/python3
"""Module containing a class BaseGeometry"""


class BaseGeometry:
    """A Class that just raises an exception"""

    def area(self):
        """Method that defines area of class

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
