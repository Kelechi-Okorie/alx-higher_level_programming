#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The square class

The square class with method for
calculating areas
"""


class Square:
    """A square class with size attribute and area method"""

    def __init__(self, size=0, position=(0, 0)):
        """The init method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """The getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, size):
        """The setter for the size attribute."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """The getter for position."""
        return self.__position

    @position.setter
    def position(self, position):
        "The setter for position attribute."""
        self.__position = position

    def area(self):
        """The area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square."""

        if self.size == 0:
            print(end="\n")
            return

        for x in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print(end="\n")
