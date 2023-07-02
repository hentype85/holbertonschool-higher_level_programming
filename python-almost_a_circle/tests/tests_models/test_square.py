#!/usr/bin/python3
"""tests square"""

from models.base import Base
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
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")


class test_Square(unittest.TestCase):
    """tests Square"""

    def test_id(self):
        """test id"""
        sq = Square(2, 0, 0, 1)
        self.assertEqual(1, sq.id)
    
    def test_width_string(self):
        """testing for other type"""
        with self.assertRaises(TypeError):
            sq = Square("a")
    
    def test_width_list(self):
        """testing for other type"""
        with self.assertRaises(TypeError):
            sq = Square([10, 6])
    
    def test_x_value(self):
        """negative x value"""
        square = Square(1)
        with self.assertRaises(ValueError):
            square.x = -2
    
    def test_y_value(self):
        """negative y value"""
        square = Square(1)
        with self.assertRaises(ValueError):
            square.y = -2

    def test_x_type(self):
        """test no int values in x"""
        sq = Square(2)
        with self.assertRaises(TypeError):
            sq.x = [1, 2, 3]
            sq.x = {1, 2}
            sq.x = "1"
            sq.x = 1.2
            sq.x = None
            sq.x = True
            sq.x = {}
            sq.x = (1, 2, 3)
            sq.x = float()

    def test_y_type(self):
        """test no int values in y"""
        sq = Square(2)
        with self.assertRaises(TypeError):
            sq.y = [1, 2, 3]
            sq.y = {1, 2}
            sq.y = "1"
            sq.y = 1.2
            sq.y = None
            sq.y = True
            sq.y = {}
            sq.y = (1, 2, 3)
            sq.y = float()
