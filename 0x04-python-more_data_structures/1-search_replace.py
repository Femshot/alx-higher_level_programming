#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurences of element search with replace"""
    new_li = list(map(lambda x: x if x != search else replace, my_list))
    return new_li
