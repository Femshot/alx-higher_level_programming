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

    def area(self):
        """Computes the Area of the Rectangle class object"""
        return (self.__width * self.__height)

    def __str__(self):
        """Determines str() output for Rectangle class object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """A derived class of Rectangle class"""

    def __init__(self, size):
        """Instantiation of Square class

            Args:
                size (int): First argument passed
        """
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """Computes area of the Square class object"""
        return (self.__size ** 2)

    def __str__(self):
        """Determines str() output for Square class object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
