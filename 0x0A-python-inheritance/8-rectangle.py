#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Module BaseGeometry
The BaseGeometry module
"""


class Rectangle(BaseGeometry):
    """Base Geometry class"""

    def __init__(self, width, height):
        """Initializes a rectangle object"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
