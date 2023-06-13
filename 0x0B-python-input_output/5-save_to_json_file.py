#!/usr/bin/python3
"""Module containing the function save_to_json_string"""
import json


def save_to_json_file(my_obj, filename):
    """Converts python object to json string representation

    stores string in an open file ready to be written

    Args:
        my_obj (any): Any python object
        filename (str): Name of file object to write to

    Return:
        JSON string representation of converted object
    """
    with open(filename, 'w', encoding="utf-8") as new_file:
        return (json.dump(my_obj, new_file))
