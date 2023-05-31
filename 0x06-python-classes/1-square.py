#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module containing a single class, Square"""


class Square:
    """Defines a square with private attribute called 'size'"""

    def __init__(self, size):
        """Initialisation of class square instance

        Atrributes:
            size: Has no type or value verification
        """
        self.__size = size
