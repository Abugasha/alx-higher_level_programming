#!/usr/bin/python3
"""linked list docstrings.

This module demonstrates how to use a linked list with classes.
"""


class Node():
    """This class defines a memory space"""
    def __init__(self, data, next_node=None):
        """ corroboares data is int and next node is valid"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """get data value"""
        return self.__data

    @property
    def next_node(self):
        """get next node value"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next node value"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(Node):
    """defines a single linked list structure"""
    def __init__(self):
        """head initialization"""
        self.__head = None

    def __str__(self):
        """in case of printing"""
        final_str = ""
        while(self.__head is not None):
            final_str += str(self.__head.data)
            if (self.__head.next_node is not None):
                final_str += "\n"
            self.__head = self.__head.next_node
        return(final_str)

    def sorted_insert(self, value):
        """insert the node in order"""
        if (self.__head is None):
            self.__head = Node(value)
            return
        if (value <= self.__head.data):
            self.__head = Node(value, self.__head)
            return
        origin = self.__head
        while (self.__head.next_node is not None):
            if (self.__head.next_node.data > value):
                self.__head.next_node = Node(value, self.__head.next_node)
                self.__head = origin
                return
            self.__head = self.__head.next_node
        self.__head.next_node = Node(value)
        self.__head = origin
