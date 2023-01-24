#!/usr/bin/python3
"""2-square docstrings.

This module demonstrates how to receive data with a class.
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
