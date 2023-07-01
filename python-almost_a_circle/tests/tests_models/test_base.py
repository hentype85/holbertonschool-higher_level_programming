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

    def test_Base(self):
        """test Base"""
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_id_none(self):
        """sending no id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """sending a valid id"""
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_id_zero(self):
        """sending an id 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """sending negative id"""
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        """sending an id that is not an int"""
        b = Base("hola")
        self.assertEqual("hola", b.id)

    def test_id_list(self):
        """sending an id that is not an int"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        """sending an id that is not an int"""
        b = Base({"id": 106})
        self.assertEqual({"id": 106}, b.id)

    def test_id_tuple(self):
        """sending an id that is not an int"""
        b = Base((7,))
        self.assertEqual((7,), b.id)

    def test_to_json_type(self):
        """test the json string"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """test the json string"""
        sq = Square(1, 0, 0, 100)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 100, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        """test the json string"""
        sq = Square(1, 0, 0, 100)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """test the json string"""
        sq = Square(1, 0, 0, 100)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
