#!/usr/bin/python3
"""Unittest base
Contains test cases for the base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for the Base class"""

    def test_task_id(self):
        """Create new instance and test for correct id"""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(-2)
        self.assertEqual(b5.id, -2)
        b6 = Base()
        self.assertEqual(b6.id, 5)

    def test_task_instance(self):
        """Test the created instance is of correct type"""

        base = Base()
        self.assertTrue(isinstance(base, Base))
        self.assertEqual(type(base), Base)
