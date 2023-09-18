#!/usr/bin/python3
""" square test file """


import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for Square class"""

    def setUp(self):
        Base._Base_nb_objects = 0

    def test_10_attributes(self):
        """Test Square class for correct attributes"""

        sq = Square(2)
        self.assertEqual(sq.id, 1)
        sq = Square(2, 5)
        self.assertEqual(sq.width, 2)
        self.assertEqual(sq.height, 2)
        sq = Square(2, 5, 10)
        self.assertEqual(sq.x, 5)
        self.assertEqual(sq.y, 10)
        sq = Square(2, 5, 10, 12)
        self.assertEqual(sq.id, 12)

    def test_10_str_(self):
        """Test Square class __str__ representation"""

        sq = Square(2, 5, 10, 12)
        self.assertEqual(str(sq), "[Square] (12) 5/10 - 2")

    def test_10_inheritance(self):
        """Test Square instance for inheritance"""

        sq = Square(2)
        self.assertTrue(type(sq) is Square)
        self.assertTrue(isinstance(sq, Square))
        self.assertTrue(isinstance(sq, Rectangle))
        self.assertTrue(isinstance(sq, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertFalse(isinstance(Square, Base))

    def test_10_exceptions(self):
        """Test Square class for missing args"""

        with self.assertRaises(TypeError) as x:
            sq = Square()
        msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(x.exception), msg)

    def test_10_inherited_from_rectangle(self):
        """Test Square for methods inherited from Rectangle"""

        sq = Square(2)
        self.assertEqual(sq.area(), 4)
        sq = Square(2, 5, 10, 12)
        sq.update(20)
        self.assertEqual(sq.id, 20)

        string_buffer = io.StringIO()
        sq = Square(4)
        with contextlib.redirect_stdout(string_buffer):
            sq.display()
        string_value = string_buffer.getvalue()
        display_value = "####\n####\n####\n####\n"
        self.assertEqual(string_value, display_value)

    def test_11_attributes(self):
        """Test Square class for size attributes"""

        sq = Square(8)
        self.assertEqual(sq.size, 8)
        sq = Square(2, 5, 10, 12)
        self.assertEqual(sq.size, 2)

    def test_11_exceptions(self):
        """Test Square class for wrong attributes"""

        with self.assertRaises(TypeError) as x:
            sq = Square("alx", 2)
        self.assertEqual(str(x.exception), "width must be an integer")

        with self.assertRaises(TypeError) as x:
            sq = Square(2, "alx")
        self.assertEqual(str(x.exception), "x must be an integer")

        with self.assertRaises(TypeError) as x:
            sq = Square(2, 5, "Foo", 12)
        self.assertEqual(str(x.exception), "y must be an integer")

        with self.assertRaises(ValueError) as x:
            sq = Square(0, 2)
        self.assertEqual(str(x.exception), "width must be > 0")

        with self.assertRaises(ValueError) as x:
            sq = Square(-1)
        self.assertEqual(str(x.exception), "width must be > 0")

        with self.assertRaises(ValueError) as x:
            sq = Square(2, -5)
        self.assertEqual(str(x.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as x:
            sq = Square(2, 5, -10, 12)
        self.assertEqual(str(x.exception), "y must be >= 0")

    def test_12_update(self):
        """Test class Square for normal attributes"""
        sq = Square(2)
        sq.update(10)
        self.assertEqual(sq.id, 10)
        sq.update(x=12)
        self.assertEqual(sq.x, 12)
        sq.update(size=3, id=14, y=40)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.id, 14)
        self.assertEqual(sq.y, 40)
        sq.update()
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.id, 14)
        self.assertEqual(sq.y, 40)

    def test_12_update_exceptions(self):
        """Test class Square for update exceptions"""

        sq = Square(2)
        with self.assertRaises(TypeError) as x:
            sq.update(2, 3, 4, "alx")
        self.assertEqual(str(x.exception), "y must be an integer")

        with self.assertRaises(TypeError) as x:
            sq.update("hello", 3, 4)
        self.assertEqual(str(x.exception), "id must be an integer")

    def test_14_to_dictionary(self):
        """Test class Square to_dictionary method"""

        sq = Square(10, 2, 1)
        sq_dict = sq.to_dictionary()
        sample_dict = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(sq_dict), len(sample_dict))
        self.assertEqual(type(sq_dict), dict)
        sq2 = Square(1, 1)
        sq2.update(**sq_dict)
        sq2_dict = sq2.to_dictionary()
        self.assertEqual(len(sq_dict), len(sq2_dict))
        self.assertEqual(type(sq2_dict), dict)
        self.assertFalse(sq == sq2)

    def test_14_to_dictionary_exception(self):
        """Test class Square to_dictionary wrong arguments"""

        with self.assertRaises(TypeError) as x:
            sq = Square(10, 2, 1, 9)
            sq_dict = sq.to_dictionary("alx")
        msg = "to_dictionary() takes 1 positional argument but 2 were given"
        self.assertEqual(str(x.exception), msg)


if __name__ == "__main__":
    unittest.main()
