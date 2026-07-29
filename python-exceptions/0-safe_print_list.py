#!/usr/bin/python3
"""Module that safely prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list and return the count printed."""
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
