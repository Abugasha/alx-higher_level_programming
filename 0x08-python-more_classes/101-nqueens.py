#!/usr/bin/python3
""" This script solves the N-Queen problem"""


import sys


def check_moves(matrix, position_x, position_y):
    """
    This function checks if a position (x, y) has
    has a 1 horizontal, vertical or diagonal
    """
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            # Si hay un 1 horizontal
            if (matrix[x][position_y] == 1):
                return(0)
            # Si hay un 1 vertical
            if (matrix[position_x][y] == 1):
                return(0)
            # Si hay un 1 diagonal abajo a la derecha
            try:
                if (matrix[position_x + x][position_y + x] == 1):
                    return(0)
            except IndexError:
                pass
            try:
                if (position_x - x >= 0):
                    if (matrix[position_x - x][position_y + x] == 1):
                        return(0)
            except IndexError:
                pass
            try:
                if (position_x - x >= 0 and position_y - x >= 0):
                    if (matrix[position_x - x][position_y - x] == 1):
                        return(0)
            except IndexError:
                pass
            try:
                if (position_y - x >= 0):
                    if (matrix[position_x + x][position_y - x] == 1):
                        return(0)
            except IndexError:
                pass
    return(1)


def put_coords(matrix, result):
    """
    This function print a pair of coords to result
    """
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if (matrix[i][j] == 1):
                result[i][0] = i
                result[i][1] = j
    return result


def recursive_chess(matrix, columns):
    """
    This function checks for every queen
    if there's a queen atacking if not print
    the n queens position
    """
    if (columns == n):
        result = [[0 for x in range(2)] for y in range(n)]
        print(put_coords(matrix, result))
        return

    for row in range(n):
        if (check_moves(matrix, row, columns) == 1):
            matrix[row][columns] = 1
            recursive_chess(matrix, columns + 1)
            matrix[row][columns] = 0


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    matrix = [[0 for j in range(n)] for i in range(n)]
    recursive_chess(matrix, 0)
