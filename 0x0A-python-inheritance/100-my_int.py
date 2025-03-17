#!/usr/bin/python3
"""Module containing class definition for MyInt"""


class MyInt(int):
    """A class that inherits from int"""

    def __eq__(self, num):
        """
        equal function for MyInt class

        Attributes:
            num (int): an inputed integer
        """
        return super().__ne__(num)

    def __ne__(self, num):
        """
        no equal function for MyInt class

        Attributes:
            num (int): an inputed integer
        """
        return super().__eq__(num)
