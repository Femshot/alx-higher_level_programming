#!/usr/bin/python3
"""Module containing a class Square, derived from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A derived class of rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of class object

        Pass all arguments to Derived class to initialise
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Defines str()utput for class

        Returns [Square] (<id>) <x>/<y> - <size> """
        return ("[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width))

    @property
    def size(self):
        """Getr for size attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of Square object

        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.size = args[arg]
                if arg == 2:
                    self.x = args[arg]
                if arg == 3:
                    self.y = args[arg]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square"""
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
