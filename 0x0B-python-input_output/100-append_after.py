#!/usr/bin/python3
""" Defines a function append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file,
    After each line containing a specific string

    Args:
        filename: The text file
        search_string: The specific string to be found in each line
        new_string: The string to insert in next line after a match of
                    search_string
    """
    with open(filename, 'r') as target:
        line = target.readlines()
        inserted_lines = 0
        for pos, string in enumerate(line.copy()):
            if string.find(search_string) != -1:
                line.insert((pos + 1 + inserted_lines), new_string)
                inserted_lines += 1

    with open(filename, 'w') as target:
        target.writelines(line)
