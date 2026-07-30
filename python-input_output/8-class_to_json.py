#!/usr/bin/python3
"""Module that defines a class_to_json function."""


def class_to_json(obj):
    """Return a JSON-serializable dictionary description of an object.

    Args:
        obj: An instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        dict: The dictionary representation of obj's attributes.
    """
    return obj.__dict__
