#!/usr/bin/python3
"""Module containing the function from_json_string"""
import json


def from_json_string(my_str):
    """Converts json string to python object representation

    Return:
        object representation of converted JSON string"""
    return (json.loads(my_str))
