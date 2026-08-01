#!/usr/bin/python3
"""Module that prints a square of a given size.

This module defines a single function, print_square, which prints a
square made of the character #.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
