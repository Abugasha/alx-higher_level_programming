#!/usr/bin/python3
"""
This document is the representation of a
square based on the characteristics of a rectangle
Written by daorejuela1
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class creates an square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Generates a square based on the rectangle

        Args:
            size (int): Square size
            x (int, optional): X position. Defaults to 0.
            y (int, optional): Y position. Defaults to 0.
            id (int, optional): Square id. Defaults to None.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        """ width setter """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Generates a string to represent the square
        """
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ Update class variables """
        if kwargs and args is None or args is ():
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

    def to_dictionary(self):
        """sends instance rep in dict format"""
        new_dict = {}
        for key, value in self.__dict__.items():
            filtered_key = key.split("_")[-1]
            if (filtered_key == "height"):
                continue
            if (filtered_key == "width"):
                filtered_key = "size"
            new_dict[filtered_key] = value
        return(new_dict)
