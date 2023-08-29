#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The square class

The square class with method for
calculating areas
"""


class Square:
    """A square class with size attribute and area method"""

    def __init__(self, size=0):
        """The init method"""
        self.size = size

    @property
    def size(self):
        """The getter."""
        return self.__size

    @size.setter
    def size(self, size):
        """The setter."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""

        for x in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print(end="\n")
