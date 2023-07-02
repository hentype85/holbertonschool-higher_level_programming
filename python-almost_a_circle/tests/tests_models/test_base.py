#!/usr/bin/python3
"""tests base"""

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
            ["../../models/base.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_base.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class test_Base(unittest.TestCase):
    """tests Base"""

    def test_id(self):
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_id_none(self):
        prueba = Base(None)
        self.assertEqual(prueba.id, 1)

    def test_to_json_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_Empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_json_type(self):
        sq = Square(1)
        json_str = Base.to_json_string([sq.to_dictionary()])
        self.assertEqual(type(json_str), str)

    def test_json_type(self):
        rc = Rectangle(2,2,1,1,100)
        json_str = Rectangle.to_json_string([rc.to_dictionary()])
        self.assertEqual(type(json_str), str)
