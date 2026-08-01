#!/usr/bin/python3
"""Module that divides all elements of a matrix by a number.

This module defines a single function, matrix_divided, which returns
a new matrix with every element divided by a given number, rounded
to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide every element of a matrix by a number.

    Args:
        matrix (list): A list of lists of integers or floats. Every
            row must be the same length.
        div (int or float): The number to divide every element by.

    Returns:
        list: A new matrix with every element divided by div,
            rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of int/float, if
            rows differ in length, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err)
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(
                    value, bool):
                raise TypeError(err)
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in row] for row in matrix]
