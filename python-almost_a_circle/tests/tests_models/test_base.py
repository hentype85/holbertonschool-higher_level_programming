#!/usr/bin/python3
"""tests base"""

from models.base import Base
from models.square import Square
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
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_base.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")


class test_Base(unittest.TestCase):
    """tests Base"""

    def test_id_none(self):
        """no id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """id"""
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        """id 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """negative id"""
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        """id is not an int"""
        b = Base("str")
        self.assertEqual("str", b.id)

    def test_id_list(self):
        """id is not an int"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        """id is not an int"""
        b = Base({"id": 100})
        self.assertEqual({"id": 100}, b.id)

    def test_id_tuple(self):
        """id is not an int"""
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        """testing json"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """testing json"""
        sq = Square(5, 1, 1, 2)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 2, "y": 1, "size": 5, "x": 1}])

    def test_to_json_None(self):
        """testing json"""
        sq = Square(1, 0, 0, 100)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """testing json"""
        sq = Square(1, 0, 0, 100)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
