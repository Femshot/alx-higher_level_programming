#!/usr/bin/python3
"""Module containing a class Square"""


class Square:
    """Defines a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialisation for class square

        Args:
            size(int): Size of intended square
            position(tuple): Two positive integars
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of current square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a private attribute size,size must always be a positve Integar

        Args:
            value(int): A positive integar to tell the size of a square

        Raises:
            TypeError: If type of size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """Takes a tuple of two positive integers

        Sets is a position coordinate for square class instance

        Args:
            value(tuple): Tuple of two positive inetegers
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__x, self.__y = value
        if type(self.__x) is not int or self.__x < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__y) is not int or self.__y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = (self.__x, self.__y)

    def area(self):
        """Defines and computes area of an instance of class square

        Return (int): self.__size * self.__size
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints out the square using '#'

        Using size for length and breath of the square printed.
        Prints an empty line if size = 0
        """
        if self.__size == 0:
            print("{}".format(""))
        else:
            if self.__y:
                print('\n' * self.__y, end="")
            for i in range(self.__size):
                if self.__x:
                    print(' ' * self.__x, end="")
                for j in range(self.__size):
                    print('#', end="")
                print("{}".format(""))

    def __str__(self):
        """Returns a square string using '#' like the my_print method"""
        square_string = ""
        if self.__size == 0:
            return square_string
        else:
            if self.__y:
                square_string += '\n' * self.__y
            for i in range(self.__size):
                if self.__x:
                    square_string += ' ' * self.__x
                for j in range(self.__size):
                    square_string += '#'
                if i is not (self.__size - 1):
                    square_string += '\n'
        return(square_string)
