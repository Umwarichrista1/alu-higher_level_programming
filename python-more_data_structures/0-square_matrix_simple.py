#!/usr/bin/python3
"""Module that squares every value in a 2D matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with every value squared."""
    return [[value ** 2 for value in row] for row in matrix]
