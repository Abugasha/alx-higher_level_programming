#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda x: list(map(lambda n: n**2, x[0:len(x)])), matrix)))

