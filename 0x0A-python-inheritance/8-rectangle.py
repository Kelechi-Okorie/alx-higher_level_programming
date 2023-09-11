#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Module BaseGeometry
The BaseGeometry module
"""


class Rectangle(BaseGeometry):
    """Rectangle class
    inherits from BaseGeometry
    private attributes:
        - width
        - height
    """

    def __init__(self, width, height):
        """Initializes a rectangle object

        Args:
            - width: with of the rectangle
            - height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
