#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("{:d} arguments.".format(num))
    elif num == 1:
        print("{:d} argument:".format(num))
    else:
        print("{:d} arguments:".format(num))
    list_args = []
    for c in argv:
        list_args += [c]
    for i in range(1, len(list_args)):
        print("{}: {}".format(i, list_args[i]))
