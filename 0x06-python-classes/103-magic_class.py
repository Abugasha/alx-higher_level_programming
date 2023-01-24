#!/usr/bin/python3
"""This module replicates a class by it's bytecode."""
import math


class MagicClass():
    """class to represent a circle"""

    def __init__(self, radius=0):
        """get radius type"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area = r^2 * pi"""
        return((self.__radius ** 2) * math.pi)

    def circumference(self):
        """circumference = 2 * r * pi"""
        return(2 * math.pi * self.__radius)
