#!/usr/bin/python3
""" Execute a function safely """
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
