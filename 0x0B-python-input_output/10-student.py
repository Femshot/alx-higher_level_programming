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
        if attrs and type(attrs) == list:
            new_dict = {}
            for item in attrs:
                if type(item) == str and (value := self.__dict__.get(item,
                    None)):
                    new_dict[item] = value
            return new_dict
        else:
            return self.__dict__
