#!/usr/bin/python3
"""tests rectangle"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import pep8
import json


class TestCodeFormat(unittest.TestCase):
    """test pep8"""

    def test_pep8_conformance(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/rectangle.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_rectangle.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class test_Rectangle(unittest.TestCase):
    """tests Rectangle"""

    def test_ok_sq_Subclass(self):
        self.assertIsInstance(Rectangle(5, 5, 2, 2, 98), Base)

    def test_arectangle_id(self):
        rect = Rectangle(1, 3, 0, 0, 209)
        self.assertEqual(209, rect.id)

    def test_width(self):
        rect = Rectangle(5, 3, 0, 0, 209)
        self.assertEqual(5, rect.width)

    def test_height(self):
        rect = Rectangle(1, 10, 0, 0, 209)
        self.assertEqual(10, rect.height)

    def test_x(self):
        rect = Rectangle(1, 3, 54, 0, 209)
        self.assertEqual(54, rect.x)

    def test_y(self):
        rect = Rectangle(1, 3, 0, 45, 209)
        self.assertEqual(45, rect.y)

    def test_str_overload(self):
        rect = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(rect.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_update_id(self):
        rect = Rectangle(5, 10, 8, 7, 88)
        rect.update(54)
        self.assertEqual(54, rect.id)

    def test_area(self):
        rect = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(rect.area(), 5 * 10)
        with self.assertRaises(TypeError):
            rect.area(1)