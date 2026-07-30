#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class inheriting a_class.

    The check only counts when obj's class inherited (directly or
    indirectly) from a_class, not when obj's class is a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj's class is a genuine subclass of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
