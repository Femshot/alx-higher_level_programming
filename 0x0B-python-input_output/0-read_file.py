#!/usr/bin/python3
"""Module containing a function read_file"""


def read_file(filename=""):
    """Reads and prints the content of a file passed into it

    Args:
        filename (str): Fil object name
    """
    with open(filename, encoding="UTF8") as this_file:
        print(this_file.read(), end="")
