#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    first_line = f"{num:d} argument{':' if num == 1 else 's'}"
    if num != 1:
        first_line = f"{first_line}{'.' if num == 0 else ':'}"
    print(first_line)
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

