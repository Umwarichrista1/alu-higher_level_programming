#!/usr/bin/python3
"""Module that prints only the integers among x elements of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integers among the first x elements, return count printed."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
