#!/usr/bin/python3
class Square:
    """Defines a class square"""
    def __init__(self, size=0):
        """Initialisation for class square

        Defines a private attribute size, instantiated with size=0
        and size must always be a positve Integar
        """
        try:
            size = size + 0
        except TypeError:
            raise TypeError("size must be an integar")
        if size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Defines and computes area of an instance of class square

        Area = self.__size * self.__size"""
        return (self.__size ** 2)
