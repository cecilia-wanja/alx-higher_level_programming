#!/usr/bin/python3
"""
    divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """Returns a matrix
    of results of a divided matrix
    """
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
