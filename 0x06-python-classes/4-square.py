#!/usr/bin/python3
"""Module containing a class Square"""


class Square:
    """Defines a class square"""

    def __init__(self, size=0):
        """Initialisation for class square

        Args:
            size(int): Size of intended square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of current square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a private attribute size,size must always be a positve Integar

        Args:
            value(int): A positive integar to tell the size of a square

        Raises:
            TypeError: If type of size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Defines and computes area of an instance of class square

        Return (int): self.__size * self.__size
        """
        return (self.__size ** 2)
