#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference_1 = set_1.difference(set_2)
    difference_2 = set_2.difference(set_1)
    difference = difference_1.union(difference_2)
    return(difference)

