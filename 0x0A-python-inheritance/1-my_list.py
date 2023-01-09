#!/usr/bin/python3
""" My List """


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        print(sorted(self))
