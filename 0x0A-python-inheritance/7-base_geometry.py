#!/usr/bin/python3
"""Module containing a class BaseGeometry"""


class BaseGeometry:
    """A Class that just raises exceptions"""

    def area(self):
        """Method that defines area of class

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates the input type of value

        Args:
            name (str): First Argument
            value (int): Second Agument

        Raises:
            TypeError: If value not an Integer
            ValueError: If value is less than or equal to zero(0)
        """
        if type(name) is str:
            pass
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
