#!/usr/bin/python3
"""Module Containing a Class Rectangle"""


class Rectangle:
    """A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation of a class Rectangle

            Args:
                width (int): The rectangle width
                height (int): The rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to get width in class Recatangle

        Return:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set properties of width attributes

        Args:
            value (int): Width of rectangle to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property to get height in class Recatangle

        Return:
            self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set properties of height attributes

        Args:
            value (int): Height of rectangle to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of the Rectangle class instance

        Return:
            width * height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of the Rectangle class instance

        Return:
            2(width + height)
        """
        if self.__width and self.__height:
            return (2 * (self.__width + self.__height))
        else:
            return 0

    def __str__(self):
        """Print a rectangle with the '#' character

        use width and height as dimensions
        """
        if self.__height and self.__width:
            rec = ""
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rec += '#'
                if i < (self.__height - 1):
                    rec += '\n'
            return rec

        else:
            return ""

    def __repr__(self):
        """Returns a string representation of the rectangle class

        it should be able to recreate a new instance by using eval()
        """
        rec = "Rectangle(" + str(self.__width) + ',' + str(self.__height) + ")"
        return rec
