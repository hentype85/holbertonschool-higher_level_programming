#!/usr/bin/python3
"""tests base"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests"""

    def test_init_with_id(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
    