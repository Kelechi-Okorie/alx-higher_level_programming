#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_max_at_the_end(self):
        """Test with normal list of ints: should return max int"""
        mylist = [1, 2, 3, 4, 5, 6]
        result = max_integer(mylist)
        self.assertEqual(result, 6)

    def test_max_at_the_beginning(self):
        """Test a list with max at the end"""
        mylist = [6, 1, 2, 3]
        result = max_integer(mylist)
        self.assertEqual(result, 6)

    def test_max_at_the_middle(self):
        """Test list with max in the middle"""
        mylist = [1, 2, 6, 3, 4]
        result = max_integer(mylist)
        self.assertEqual(result, 6)

    def test_one_negative_number(self):
        """Test list with one negative number"""
        mylist = [1, 2, -3, 4, 5]
        result = max_integer(mylist)
        self.assertEqual(result, 5)

    def test_only_negative_numbers(self):
        """Test list of negative ints only: should return the max"""
        mylist = [-1, -2, -3, -4, -5, -6]
        result = max_integer(mylist)
        self.assertEqual(result, -1)

    def test_one_element(self):
        """Test list of one int: should return the int"""
        mylist = [1]
        result = max_integer(mylist)
        self.assertEqual(result, 1)

    def test_empty_list(self):
        """Test with empty list"""
        mylist = []
        result = max_integer(mylist)
        self.assertEqual(result, None)

    def test_same_int(self):
        """Test list with same int: should return the int"""
        mylist = [1, 1, 1, 1]
        result = max_integer(mylist)
        self.assertEqual(result, 1)


    def test_none(self):
        """Test with None as parameter: should raise TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    if __name__ == "__main__":
        unittest.main()
