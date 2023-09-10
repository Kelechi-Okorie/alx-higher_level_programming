#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def normal_test(self):
        """Test with normal list of ints: should return max int"""
        mylist = [1, 2, 3, 4, 5, 6]
        result = max_integer(mylist)
        self.assertEqual(result, 6)

    def test_no_int(self):
        """Test a list of non ints and ints:
        should raise a TypeError exception"""
        mylist = [1, 2, 3, "a", "b"]
        self.assertRaises(TypeError, max_integer, mylist)

    def test_empty_list(self):
        """Test empty list: should return None"""
        mylist = []
        result = max_integer(mylist)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test list of negative ints only: should return the max"""
        mylist = [-1, -2, -3, -4, -5, -6]
        result = max_integer(mylist)
        self.assertEqual(result, -1)

    def test_single(self):
        """Test list of one int: should return the int"""
        mylist = [1]
        result = max_integer(mylist)
        self.assertEqual(result(1))

    def test_same_int(self):
        """Test list with same int: should return the int"""
        mylist = [1, 1, 1, 1]
        result = max_integer(mylist)
        self.assertEqual(result, 1)

    def test_float(self):
        """Test list of ints and floats: should return the max"""
        mylist = [1, 2.5, 3, 4.5, 5, 6.1]
        result = max_integer(mylist)
        self.assertEqual(result(6.1))

    def test_none(self):
        """Test with None as parameter: should raise TypeError"""
        self.ssertRaises(TypeError, max_integer, None)

    def test_strings(self):
        """Test list of strings: should return the first string"""
        mylist = ["hello", "world"]
        self.assertEqual("hello")

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    if __name__ == "__main__":
        unittest.main()
