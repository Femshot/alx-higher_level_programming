#!/usr/bin/python3
"""Module caontaining a class Base"""


class Base:
    """Manages id attribute of all classes instance including derived classes

    Atrributes:
        nb_objects (int): Serves as default id counter where none is given
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base class object

        Args:
            id (int): id of object created
        """
        if id is not None:
            if type(id) is not int or id != id or id + 1 == id:
                raise TypeError("id must be an integer")
            else:
                self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
