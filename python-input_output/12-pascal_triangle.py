#!/usr/bin/python3
"""Module that defines a pascal_triangle function."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
