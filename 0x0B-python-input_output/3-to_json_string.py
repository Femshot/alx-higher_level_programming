#!/usr/bin/python3
"""Module containing the function to_json_string"""
import json


def to_json_string(my_obj):
    """Converts python object to json string representation

    Return:
        JSON string representation of converted object
    """
    return (json.dumps(my_obj))
