#!/usr/bin/python3
""" Module conatatining a simple Student class """


class Student:
    """ A simple Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialiser for Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary of an instance attribute

        Args:
            attrs: List of strings that are attributes names to retrive if
            present in instance

        """
        if type(attrs) is list:
            new_dict = {}
            for item in attrs:
                value = self.__dict__.get(item, None)
                if value:
                    new_dict[item] = value
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for key, value in json.items():
            self.__dict__[key] = value
