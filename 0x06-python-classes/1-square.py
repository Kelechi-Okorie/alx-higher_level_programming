#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" The square module.

A square module with a size attribute
"""


class Square:
    """A square class with a size"""

    def __init__(self, size):
        """The init method for the class
        Args:
            size (int): size of the square
        """
        self.__size = size
