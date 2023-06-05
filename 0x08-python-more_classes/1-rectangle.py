#!/usr/bin/python3
"""Module Containing a Class Rectangle"""


class Rectangle:
    """A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation of a class Rectangle

            Args:
                width (int): The rectangle width
                height (int): The rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to get width in class Recatangle

        Return:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set properties of width attributes

        Args:
            value (int): Width of rectangle to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property to get height in class Recatangle

        Return:
            self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set properties of height attributes

        Args:
            value (int): Height of rectangle to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
