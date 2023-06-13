#!/usr/bin/python3
Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle
Rectangle2 = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

print(issubclass(Rectangle2, BaseGeometry))
print(issubclass(Square, Rectangle))
