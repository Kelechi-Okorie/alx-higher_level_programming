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

    def test_15_to_json_string(self):
        """Test to_json static method with valid arguments"""

        my_dict = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        my_json = Base.to_json_string([my_dict])
        self.assertTrue(isinstance(my_dict, dict))
        self.assertTrue(isinstance(my_json, str))
        self.assertCountEqual(
                my_json, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_dict_1 = Base.to_json_string([])
        self.assertEqual(json_dict_1, "[]")
        json_dict_2 = Base.to_json_string(None)
        self.assertEqual(json_dict_1, "[]")

    def test_15_exception(self):
        """Test to_json_string static method with wrong arguments"""

        msg = "list_dictionaries must be a list of dictionaries"

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(2)
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string("alx")
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string([1, 2, 3, 4])
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(["alx", "school"])
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(2.3)
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string({1: 'alx', 2: 'school'})
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string((1, 2))
        self.assertEqual(str(x.exception), msg)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(True)
        self.assertEqual(str(x.exception), msg)

    def test_15_exception(self):
        """Testing Base class to_json_string method with wrong arguments"""

        msg1 = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        msg2 = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(str(x.exception), msg1)

        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(str(x.exception), msg2)

if __name__ == "__main__":
    unittest.main()
