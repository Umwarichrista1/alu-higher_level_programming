#!/usr/bin/python3
"""Module that adds two integers.

This module defines a single function, add_integer, which adds two
numbers together after validating and casting them to integers.
"""


def add_integer(a, b=98):
    """Add two integers together, casting floats to int first.

    Args:
        a (int or float): The first value to add.
        b (int or float): The second value to add. Defaults to 98.

    Returns:
        int: The sum of a and b, as an integer.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
