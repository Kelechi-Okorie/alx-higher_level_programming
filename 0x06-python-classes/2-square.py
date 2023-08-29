#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" The square class.

The class now reaise exception if size if wrong
"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """The init method

        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
