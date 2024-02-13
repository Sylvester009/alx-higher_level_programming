#!/usr/bin/python3
# tests/test_base.py

"""
Unittest for Base Class

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """defines a class TestBase"""
    def test_with_id(self):
        my_base = Base(20)
        self.assertEqual(my_base.id, 20)

    def test_without_id(self):
        my_base1 = Base()
        my_base2 = Base()
        self.assertEqual(my_base1.id, 1)
        self.assertEqual(my_base2.id, 2)


if __name__ == '__main__':
    unittest.main()
    """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):

    def test_create_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        
        # Save rectangles to file
        Rectangle.save_to_file([r1, r2])
        
        # Load rectangles from file
        loaded_rectangles = Rectangle.load_from_file()
        
        # Check if loaded rectangles are equal to original ones
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].to_dictionary(), r1_dict)
        self.assertEqual(loaded_rectangles[1].to_dictionary(), r2_dict)
        
        # Clean up created file
        os.remove("Rectangle.json")

    def test_create_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        s1_dict = s1.to_dictionary()
        s2_dict = s2.to_dictionary()
        
        # Save squares to file
        Square.save_to_file([s1, s2])
        
        # Load squares from file
        loaded_squares = Square.load_from_file()
        
        # Check if loaded squares are equal to original ones
        self.assertEqual(len(loaded_squares), 2)
        self.assertEqual(loaded_squares[0].to_dictionary(), s1_dict)
        self.assertEqual(loaded_squares[1].to_dictionary(), s2_dict)
        
        # Clean up created file
        os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()

