#!/usr/bin/python3
# tests/test_base.py

"""
Unittest for Base Class
"""

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
