#!/usr/bin/python3
"""Unittest module for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_is_base_instance(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_width_height_x_y(self):
        """Test that width, height, x and y are set correctly."""
        r = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(2, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_type_error(self):
        """Test that a non-integer width raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_value_error(self):
        """Test that a width <= 0 raises ValueError."""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_type_error(self):
        """Test that a non-integer x raises TypeError."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_value_error(self):
        """Test that a y < 0 raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test the area() method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update() with no-keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update() with keyworded arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (1) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Test the to_dictionary() method."""
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """Test using a dictionary to update another instance to an
        equal state."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main() 
