#!/usr/bin/python3
""" This is an example on how to create a locked class """


class LockedClass:
    """  Class that only accept as attribute first_name  """
    __slots__ = ['first_name']
