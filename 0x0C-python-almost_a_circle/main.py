#!/usr/bin/python3
from models.rectangle import Rectangle

if __name__ == "__main__":


    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    r3 = Rectangle(2, 3, 2, 2)
    r3.display()

    print("---")

    r4 = Rectangle(3, 2, 1, 0)
    r4.display()
