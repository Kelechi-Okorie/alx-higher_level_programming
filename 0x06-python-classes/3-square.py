#!/usr/bin/python3

class Square:
    """A square class with size attribute and area method"""

    def __init__(self, size=0):
        """The init method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """The area of the square"""
        return self.__size * self.__size
