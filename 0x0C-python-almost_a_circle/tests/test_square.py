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
        self.assertEquals(string_value, display_value)

    def test_11_attributes(self):
        """Test Square class for size attributes"""

        sq = Square(8)
        self.assertEqual(sq.size, 8)
        sq = Square(2, 5, 10, 12)
        self.assertEqual(sq.size, 2)

    def test_11_exceptions(self):
        """Test Square class for wrong attributes"""

        with self.assertRaises(TypeError) as x:
            s = Square("alx", 2)
        self.assertEqual(str(x.exception), "width must be an integer")


if __name__ == "__main__":
    unittest.main()
