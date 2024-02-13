#!/usr/bin/python3

"""
Unittest for Rectangle Class"""

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    """Test case for the Rectangle class."""

    def test_initialization(self):
        """Test the constructor."""
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_width(self):
        """Test the width property."""
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height(self):
        """Test the height property."""
        rect = Rectangle(5, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_property(self):
        """Test the x property."""
        rect = Rectangle(5, 10)
        rect.x = 7
        self.assertEqual(rect.x, 7)

    def test_y(self):
        """Test the y property."""
        rect = Rectangle(5, 10)
        rect.y = 8
        self.assertEqual(rect.y, 8)

if __name__ == "__main__":
    unittest.main()
