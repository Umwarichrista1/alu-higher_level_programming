#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test a list already in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list in no particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test a list already in descending order."""
        self.assertEqual(max_integer([9, 5, 3, 1]), 9)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test calling with no argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test a list of all negative numbers."""
        self.assertEqual(max_integer([-5, -1, -10]), -1)

    def test_duplicate_max(self):
        """Test a list with the max value appearing more than once."""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)


if __name__ == "__main__":
    unittest.main()
