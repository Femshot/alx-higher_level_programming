#!/usr/bin/python3
"""Module containing a class BaseGeometry and class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A derived class of Rectangle class"""

    def __init__(self, size):
        """Instantiation of Square class

            Args:
                size (int): First argument passed
        """
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(width=size, height=size)

    def area(self):
        """Computes area of the Square class object"""
        return (self.__size ** 2)
