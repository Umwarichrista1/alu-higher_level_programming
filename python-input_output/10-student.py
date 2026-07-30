#!/usr/bin/python3
"""Module that defines a Student class with a filterable to_json."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to keep.
                If given, only those attributes are included in the
                result. Otherwise all attributes are included.

        Returns:
            dict: The (optionally filtered) attribute dictionary.
        """
        if attrs is not None and type(attrs) is list:
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
