#!/usr/bin/python3
"""Module that prints text with extra newlines after ., ? and :.

This module defines a single function, text_indentation, which
prints a block of text with two newlines inserted after every
occurrence of ".", "?", or ":".
"""


def text_indentation(text):
    """Print text with two newlines after each ., ? or : character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    stripped = text.strip()
    line = ""
    for char in stripped:
        if char == " " and len(line) == 0:
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
