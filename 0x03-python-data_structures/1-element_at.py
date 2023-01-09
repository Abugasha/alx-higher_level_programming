#!/usr/bin/python3
def element_at(my_list, idx):
    """Gets element in list, if not found returns None"""
    if (idx + 1 > len(my_list) or idx < 0):
        return (None)
    else:
        return(my_list[idx])

