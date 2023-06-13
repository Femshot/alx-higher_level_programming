#!/usr/bin/python3
"""Module containing a function write_file"""


def write_file(filename="", text=""):
    """Writes a string of text to a given text file

    Args:
        filename (str): Name of file object to write to
        text (str): Text to write into file object

    Return:
        Number of characters written to file object
    """
    with open(filename, 'w', encoding="UTF8") as this_file:
        count = this_file.write(text)
        return count
