#!/usr/bin/python3
"""Module caontaining a class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries == [] or list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        file = "{}.json".format(cls.__name__)
        new = []
        with open(file, 'w') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                for obj in list_objs:
                    new.append(obj.to_dictionary())
                f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))
