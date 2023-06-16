#!/usr/bin/python3
"""Module contaning the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A derived class of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of class object

        Args:
            width (int): The first argument
            height (int): The second argument
            x (int): The third argument
            y (int): The fourth argument
            id (int): id of objet instance
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width attribute"""
        if type(width) is not int or width != width or width + 1 == width:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height attribute"""
        if type(height) is not int or height != height or height + 1 == height:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x attribute"""
        if type(x) is not int or x != x or x + 1 == x:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for x attribute"""
        if type(y) is not int or y != y or y + 1 == y:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates area of the class object"""
        return (self.__width * self.__height)

    def display(self):
        """Prints rectangle object with # character

        dimensions based on width and height values
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, "#" * self.__width, sep='')

    def __str__(self):
        """Defines str()utput for class

        Returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return ("[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height))
