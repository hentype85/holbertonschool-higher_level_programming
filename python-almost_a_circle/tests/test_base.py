#!/usr/bin/python3

import unittest
from models.base import Base
import pep8


class TestBase(unittest.TestCase):
    """tests"""

    def test_pep8_conformance(self):
        """Test PEP 8"""
        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors,
            0,
            msg="PEP 8 violations:\n\n" + "\n".join(result.messages)
            )

    def test_init_with_id(self):
        obj = Base(id=1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_to_json_string(self):
        obj = Base(id=1)
        json_str = obj.to_json_string([obj.to_dictionary()])
        expected = '[{"id": 1}]'
        self.assertEqual(json_str, expected)

    def test_save_to_file(self):
        obj1 = Base(id=1)
        obj2 = Base(id=2)
        Base.save_to_file([obj1, obj2])

    def test_save_to_file(self):
        obj1 = Base(id=1)
        obj2 = Base(id=2)
        Base.save_to_file([obj1, obj2])

    def test_save_to_file(self):
        obj1 = Base(id=1)
        obj2 = Base(id=2)
        Base.save_to_file([obj1, obj2])

    def test_load_from_file(self):
        objs = Base.load_from_file()
