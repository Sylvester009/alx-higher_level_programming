#!/usr/bin/python3

"""
unittest for square class"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test case for the Square class."""

    def test_initialization(self):
        """Test the constructor."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_str_method(self):
        """Test the __str__ method."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size(self):
        """Test the size property."""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_size_property_with_width_and_height(self):
        """Test the size property when width and height are set directly."""
        square = Square(5)
        square.width = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

if __name__ == "__main__":
    unittest.main()
