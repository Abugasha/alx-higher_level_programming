#!/usr/bin/python3
"""5-square docstrings.

This module demonstrates how to use print with classes.
"""


class Square():
    """This class defines a Square """
    def __init__(self, size=0):
        """Initialize square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        """prints the square with #"""
        if (self.__size == 0):
            print()
            return

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
