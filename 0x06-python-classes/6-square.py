#!/usr/bin/python3
"""2-square docstrings.

This module demonstrates how to use get/set methods.
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
        if (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
