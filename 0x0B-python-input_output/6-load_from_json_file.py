#!/usr/bin/python3
"""Module containing the function load_from_json_string"""
import json


def load_from_json_file(filename):
    """Converts json file to python object representation

    Args:
        filename (str): Name of json file object to read from

    Return:
        Python object
    """
    with open(filename, 'r', encoding="utf-8") as new_file:
        return (json.load(new_file))
