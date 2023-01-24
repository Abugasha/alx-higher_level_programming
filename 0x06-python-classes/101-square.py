#!/usr/bin/python3
"""linked list docstrings.

This module demonstrates how to use print with square.
"""


class Square():
    """This class defines a Square """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __str__(self):
        """creates a string with the square and #"""
        final_string = ""
        if (self.__size == 0):
            return final_string
        for lines in range(0, self.__position[1]):
            final_string += "\n"
        for i in range(0, self.__size):
            for spaces in range(0, self.__position[0]):
                final_string += " "
            for j in range(0, self.__size):
                final_string += "#"
            if (i != self.__size - 1):
                final_string += "\n"
        return(final_string)

    def area(self):
        """Returns the square area -> a * b"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the actual square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method that updates size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """this will retrieve the position tuple"""
        return self.__position

    @position.setter
    def position(self, value):
        """this will set the position tuple"""
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """prints the square with #"""
        if (self.__size == 0):
            print()
            return
        for lines in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for spaces in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
