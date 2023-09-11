#!/usr/bin/python3
"""Module BaseGeometry
The BaseGeometry module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    inherits from Rectangle
    private attributes:
        - size
    """

    def __init__(self, size):
        """Initializes a square object

        Args:
            - size: size of the square
        """
        self.integer_validator("size", size)

        self.__size = size

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """calculates the area of the rectangle
        Overwrites the area() method from its parent
        """

        return self.__size * self.__size
