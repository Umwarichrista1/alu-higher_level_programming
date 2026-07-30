#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """Represent a list that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
