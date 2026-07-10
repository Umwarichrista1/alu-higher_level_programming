#!/usr/bin/python3
"""Module that adds or replaces a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Add or replace key with value in a_dictionary, then return it."""
    a_dictionary[key] = value
    return a_dictionary
