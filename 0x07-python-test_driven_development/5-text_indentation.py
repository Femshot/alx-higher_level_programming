#!/usr/bin/python3
"""Module containing a function text_indentation"""


def text_indentation(text):
    """Prints a string with 2 new lines after '.', '?', and ':'

    Args:
        text (str): text to print

    Raises:
        TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')

    print(string, end='')
