#!/usr/bin/python3
"""Module that replaces occurrences of an element in a list."""


def search_replace(my_list, search, replace):
    """Return a new list with all `search` values replaced by `replace`."""
    return [replace if item == search else item for item in my_list]
