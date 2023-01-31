#!/usr/bin/python3
"""

matrix_divide a new matrix divided by div
written by: daorejuela1
MIT License

"""


def matrix_divided(matrix, div):
    """
    This divides a matrix by a number div.

    Args:
        matrix: first number.
        div: second number.

    Returns:
        return each element divided by div.

    Raises:
        TypeError: not a matrix,
        or not numbers, or uneven rows.
    """
    err_message = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(err_message)
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(err_message)
    # Check for all data in the matrix
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if (type(matrix[i][j]) not in [int, float]):
                raise TypeError(err_message)
    # Check for row sizes
    normal_size = len(matrix[0])
    for i in range(0, len(matrix)):
        if (normal_size != len(matrix[i])):
            raise TypeError("Each row of the matrix must have the same size")
    # Check for datatype of div
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    # Divison by zero case
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_matrix = [x[:] for x in matrix]
    for i in range(0, len(new_matrix)):
        for j in range(0, len(new_matrix[0])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    return (new_matrix)
