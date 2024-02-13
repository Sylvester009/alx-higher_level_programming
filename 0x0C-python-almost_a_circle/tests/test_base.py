#!/usr/bin/python3
# tests/test_base.py

"""
Unittest for Base Class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """defines a class TestBase"""
    def test_with_id(self):
        my_base = Base(20)
        self.assertEqual(my_base.id, 20)
        base_inst = Base(42)
        self.assertEqual(base_inst.id, 42)

    def test_without_id(self):
        my_base = Base()
        my_base2 = Base()
        self.assertEqual(my_base.id, 3)
        self.assertEqual(my_base2.id, 4)


if __name__ == '__main__':
    unittest.main()
