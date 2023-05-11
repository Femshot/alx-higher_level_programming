#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = []
    for c in argv:
        l += [c]
    result = 0
    for i in range(1, len(l)):
        result += int(l[i])
    print("{:d}".format(result))
