#!/usr/bin/python3
# tests/test_base.py

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        my_base = Base(10)
        self.assertEqual(obj.id, 10)

    def test_init_without_id(self):
        my_base1 = Base()
        my_base2 = Base()
        self.assertEqual(my_base1.id, 3)
        self.assertEqual(my_base2.id, 4)

if __name__ == '__main__':
    unittest.main()
