#!/usr/bin/python3
""" Module containing a Class to Json helper function """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure """
    return obj.__dict__
