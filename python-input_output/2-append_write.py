#!/usr/bin/python3
"""Module that defines an append_write function."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file.

    Args:
        filename (str): The path of the file to append to.
        text (str): The text to add at the end of the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
