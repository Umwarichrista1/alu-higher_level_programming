#!/usr/bin/python3
"""Module that converts a Roman numeral string to an integer."""


def roman_to_int(roman_string):
    """Convert a Roman numeral string to its integer value."""
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    previous_value = 0

    for char in reversed(roman_string):
        if char not in roman_values:
            return 0
        value = roman_values[char]
        if value < previous_value:
            total -= value
        else:
            total += value
            previous_value = value

    return total
