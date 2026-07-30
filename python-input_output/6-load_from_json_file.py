#!/usr/bin/python3
"""Module that defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Create a Python object from the content of a JSON file.

    Args:
        filename (str): The path of the JSON file to read.

    Returns:
        The Python object represented by the file content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
