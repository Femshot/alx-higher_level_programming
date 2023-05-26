#!/usr/bin/python3
def best_score(a_dictionary):
    """gets the best value from a dictionary (greatest integer)"""
    best = 0
    best_stu = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > best:
                best = value
                best_stu = key
    return best_stu
