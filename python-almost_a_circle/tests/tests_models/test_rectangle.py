#!/usr/bin/python3
"""tests rectangle"""

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
            ["../../models/rectangle.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_rectangle.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")


class test_Rectangle(unittest.TestCase):
    """tests Rectangle"""

    def test_Rectangle(self):
        """test Rectangle"""
        r = Rectangle(1, 1)
        self.assertEqual(r.id, 3)
