#!/usr/bin/python3
"""tests square"""

from models.square import Square
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
            ["../../models/square.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class test_Square(unittest.TestCase):
    """tests Square"""

    def test_ok_sq_Subclass(self):
        self.assertIsInstance(Square(1), Rectangle)
    
    def test_one_and_only_arg(self):
        sq = Square(5)
        self.assertEqual(sq.id, 3)
    
    def test_access_and_setter_w(self):
        with self.assertRaises(AttributeError):
            Square(1, 5, 5, 98).__width
    
    def test_access_and_setter_h(self):
        with self.assertRaises(AttributeError):
            Square(1, 5, 5, 98).__height
    
    def test_access_and_setter_x(self):
        with self.assertRaises(AttributeError):
            Square(1, 5, 5, 98).__x
    
    def test_access_and_setter_y(self):
        with self.assertRaises(AttributeError):
            Square(1, 5, 5, 98).__y

    def test_access_and_setter_size(self):
        with self.assertRaises(ValueError):
            Square(1, 5, 5, 98).size = 0
    
    def test_x_notInt(self):
        with self.assertRaises(TypeError):
            Square(1, "ABC", 5, 98)
    
    