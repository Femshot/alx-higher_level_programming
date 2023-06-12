#!/usr/bin/python3
"""Module containing a class BaseGeometry and class Rectangle"""


class BaseGeometry:
    """A Class that defines a BaseGeometry"""

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

class Rectangle(BaseGeometry):
    """A derivd class of BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation of Rectangle class

            Args:
                width (int): First argument passed
                height (int): Second argument passed
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
