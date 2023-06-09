#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""
    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_negative(self):
        negative = [-2, -8, -1, -3]
        self.assertEqual(max_integer(negative), -1)
    
    def test_outofindex(self):
        out = [3, 4, 1, 7, 5, 8]
        self.assertEqual(max_integer(out), 8)

    def test_one_element_list(self):
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_zero(self):
        zeros = [0, 0, 0, 0]
        self.assertEqual(max_integer(zeros), 0)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        floats = [1.53, 6.33, -9.123, -1.54, 8.0]
        self.assertEqual(max_integer(floats), 8.0)
    
    def test_negatives_in_order(self):
        negative = [-2, -3, -4, -8]
        self.assertEqual(max_integer(negative), -2)


if __name__ == "__main__":
    unittest.main()
