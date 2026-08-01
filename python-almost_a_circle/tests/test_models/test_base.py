#!/usr/bin/python3
"""Unittest module for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_public(self):
        """Test that a given id is assigned as-is."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Test that id is auto-assigned when not given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_string(self):
        """Test that id can be set to any type without validation."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_string), list_dicts)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """Test from_json_string with a valid JSON string."""
        json_string = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(
            Base.from_json_string(json_string), [{"id": 1}, {"id": 2}])

    def test_save_to_file_none(self):
        """Test save_to_file with None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Test save_to_file with a list of Rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_list(self):
        """Test load_from_file after saving a list of Rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(r1))
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """Test create() returns a Rectangle with matching attributes."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create() returns a Square with matching attributes."""
        s1 = Square(5, 1, 2, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
