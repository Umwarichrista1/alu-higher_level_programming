#!/usr/bin/python3
"""Module that defines a lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: The attributes and methods available on obj.
    """
    return dir(obj)
