#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv)
    print("{:d} arguments:".format(num - 1))
    l = []
    for c in argv:
        l += [c]
    for i in range(1, len(l)):
        print("{}: {}".format(i, l[i]))
