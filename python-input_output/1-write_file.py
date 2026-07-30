#!/usr/bin/python3
"""Module that defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, creating or overwriting it.

    Args:
        filename (str): The path of the file to write.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
