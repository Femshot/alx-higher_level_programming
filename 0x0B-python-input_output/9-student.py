#!/usr/bin/python3
""" Module conatatining a simple Student class """


class Student:
    """ A simple Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialiser for Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dictionary of an instance attribute """
        return self.__dict__
