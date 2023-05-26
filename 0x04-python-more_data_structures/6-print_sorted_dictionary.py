#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    new_dict = sorted(a_dictionary)
    for a in new_dict:
        print("{}: {}".format(a, a_dictionary[a]))
