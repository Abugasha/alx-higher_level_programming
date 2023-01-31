#!/usr/bin/python3
"""
This document describes a function that repeats the name of somebody else

"""


def say_my_name(first_name, last_name=""):
    """
    This function is able to print a name.

    Args:
        param1: first_name.
        param2: last_name.

    Returns:
        Nothing.

    Raises:
        TypeError: if args are not strings.
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
