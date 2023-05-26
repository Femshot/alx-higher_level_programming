#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integars in a list"""
    new_list = list(set(my_list))
    res = 0
    for num in new_list:
        res += num
    return res
