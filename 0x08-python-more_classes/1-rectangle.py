#!/usr/bin/python3
""" This documents declares the class rectangle """


class Rectangle ():
    """ This class is the rectangle definition """
    def __init__(self, width=0, height=0):
        """
        This creates the instance of a new rectangle.

        Args:
            width: axis x number of element.
            height: axis y number of element.

        Raises:
            TypeError: data not a int
            ValueError: data below zero
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
