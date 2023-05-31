#!/usr/bin/python3
# -*- coding:utf-8 -*-
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
        try:
            size = size + 0
        except TypeError:
            raise TypeError("size must be an integar")
        if size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
