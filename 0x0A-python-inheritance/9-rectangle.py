#!/usr/bin/python3
"""Module containing a class BaseGeometry and class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A derived class of BaseGeometry class"""

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
        """Computes the Area of the rectangle class object"""
        return (self.__width * self.__height)

    def __str__(self):
        """Determines str() output for rectangle class object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
