#!/usr/bin/python3
"""Module that defines a read_file function."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): The path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
