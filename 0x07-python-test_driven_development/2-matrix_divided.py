#!/usr/bin/python3
"""
Divide a matrix

Return the result
"""


def matrix_divided(matrix, div):
    """
    2 parameters the matrix and the divisor
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    sizeOfRows = None
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if sizeOfRows is None:
            sizeOfRows = len(rows)
        elif sizeOfRows != len(rows):
            raise TypeError("Each row of the matrix must have the same size")
        for elements in rows:
            if type(elements) is not int and type(elements) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    return [[round(elements / div, 2) for elements in rows] for rows in matrix]
