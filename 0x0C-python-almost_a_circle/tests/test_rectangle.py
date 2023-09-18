#!/usr/bin/python3
"""Test for rectangle
Test module for the rectangle class
"""


import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class
    Inherits from the Base class
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_ids(self):
        """Test rectangle class for correct ids"""

        rect = Rectangle(10, 2)
        self.assertEqual(rect.id, 1)
        rect = Rectangle(2, 10)
        self.assertEqual(rect.id, 2)
        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.id, 12)
        rect = Rectangle(10, 2, 0, 0, -2)
        self.assertEqual(rect.id, -2)

    def test_2_attributes(self):
        """Test rectangle class for correct attribute values"""

        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        rect = Rectangle(10, 2, 6, 12, 24)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 12)
    
    def test_2_inheritance(self):
        """Test rectangle class for correct inheritance"""

        rect = Rectangle(10, 2)
        self.assertTrue(isinstance(rect, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(type(rect) is Rectangle)
        self.assertFalse(isinstance(Rectangle, Base))

    def test_2_exceptions(self):
        """Test rectangle class for exceptions"""

        with self.assertRaises(TypeError) as  x:
            rect = Rectangle(10)

        msg = "__init__() missing 1 required positional argument: 'height'"
        the_exception = x.exception
        self.assertEqual(str(the_exception), msg)

        with self.assertRaises(TypeError) as x:
            rect = Rectangle()

        msg = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        the_exception = x.exception
        self.assertEqual(str(the_exception), msg)

    def test_3_wrong_attributes(self):
        """Test rectangle class for wrong attributes"""

        with self.assertRaises(TypeError) as x:
            rect = Rectangle("Hello", 2)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "width must be an integer")
        
        
        with self.assertRaises(ValueError) as x:
            rect = Rectangle(0, 2)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "width must be > 0")

        with self.assertRaises(ValueError) as x:
            rect = Rectangle(-10, 2)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "width must be > 0")
        
        with self.assertRaises(TypeError) as x:
            rect = Rectangle(10, "hello")
        the_exception = x.exception
        self.assertEqual(str(the_exception), "height must be an integer")

        with self.assertRaises(ValueError) as x:
            rect = Rectangle(10, 0)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "height must be > 0")

        with self.assertRaises(ValueError) as x:
            rect = Rectangle(10, -2)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "height must be > 0")

        with self.assertRaises(TypeError) as x:
            rect = Rectangle(10, 2, "Hello", 3)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "x must be an int")

        with self.assertRaises(ValueError) as x:
            rect = Rectangle(10, 2, -1, 3)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "x must be >= 0")

        with self.assertRaises(TypeError) as x:
            rect = Rectangle(10, 2, 1, "Hello")
        the_exception = x.exception
        self.assertEqual(str(the_exception), "y must be an int")

        with self.assertRaises(ValueError) as x:
            rect = Rectangle(10, 2, 1, -3)
        the_exception = x.exception
        self.assertEqual(str(the_exception), "y must be >= 0")

    def test_4_area_with_normal_args(self):
        """Test area works with normal args"""

        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

        rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect.area(), 56)

    def test_4_area_with_excecptions(self):
        """Test call to area raises right exception on error"""

        with self.assertRaises(TypeError) as x:
            rect = Rectangle(3, 2)
            rect.area("Area")
        msg = "area() takes 1 positional argument but 2 were given"
        the_exception = x.exception
        self.assertEqual(str(the_exception), msg)

    def test_5_display(self):
        """Test call to display"""

        string_buffer = io.StringIO()
        rect = Rectangle(3, 2)
        with contextlib.redirect_stdout(string_buffer):
            rect.display()
        buffer_value = string_buffer.getvalue()
        display_value = "###\n###\n"
        self.assertEqual(buffer_value, display_value)

    def test_5_with_exceptions(self):
        """Test with exception"""

        with self.assertRaises(TypeError) as x:
            rect = Rectangle(10, 2)
            rect.display(9)
        msg = "display() takes 1 positional argument but 2 were given"
        the_exception = x.exception
        self.assertEqual(str(the_exception), msg)

    def test_6_str(self):
        """Test call to __str__"""

        string_buffer = io.StringIO()
        rect = Rectangle(4, 6, 2, 1, 12 )
        with contextlib.redirect_stdout(string_buffer):
            print(rect)
        buffer_value = string_buffer.getvalue()
        display_value = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(buffer_value, display_value)

    def test_7_display(self):
        """Test call to display"""

        string_buffer = io.StringIO()
        rect = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(string_buffer):
            rect.display()
        buffer_value = string_buffer.getvalue()
        display_value = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(buffer_value, display_value)

    def test_8_update(self):
        """Test call to update function"""

        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual(rect.id, 89)
        rect.update(89, 2)
        self.assertEqual(rect.width, 2)
        rect.update(89, 2, 3)
        self.assertEqual(rect.height, 3)
        rect.update(89, 2, 3, 4)
        self.assertEqual(rect.x, 4)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(rect.y, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_8_exceptions(self):
        """Test call to update with wrong arguments"""

        rect = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            rect.update("alx")
        the_exception = x.exception
        self.assertEqual(str(the_exception), "id must be an integer")

        with self.assertRaises(TypeError) as x:
            rect.update(89, 2, "alx")
        the_exception = x.exception
        self.assertEqual(str(the_exception), "height must be an integer")


        
if __name__ == "__main__":
    unittest.main()
