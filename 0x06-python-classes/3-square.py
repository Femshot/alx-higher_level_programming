#!/usr/bin/python3
"""Module containing a class Square"""


class Square:
    """Defines a class square"""

    def __init__(self, size=0):
        """Initialisation for class square

        Defines a private attribute size, instantiated with size=0
        and size must always be a positve Integar

        Attributes:
            size (int): A positive integar to tell the size of a square

        Raises:
            TypeError: If typeerror is encountered for size
            ValueError: If size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Defines and computes area of an instance of class square

        Return (int): self.__size * self.__size
        """
        return (self.__size ** 2)
