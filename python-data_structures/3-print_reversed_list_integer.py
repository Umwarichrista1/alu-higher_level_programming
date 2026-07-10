#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        if isinstance(i, int) and not isinstance(i, bool):
            print("{:d}".format(i))
