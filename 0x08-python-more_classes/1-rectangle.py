#!/usr/bin/python3
""" Rectangle class bases on 0-rectangle.py """


class Rectangle:
    """ Rectangle class bases on 0-rectangle """

    def __init__(self, width=0, height=0):
        """ Constructor for rectangle class

        Args:
            - wdith: with of the rectangle instance
            - height: height of the rectangle instance

        Returns: Nothing
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width of the instance

        Returns: width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, width):
        """ sets the width of the instance

        Args
            - width: the new width

        Returns: nothing
        """

        if type(width) is not int:
            return TypeError('width must be an integer')

        if width < 0:
            return ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        """ returns the height of the rectangle

        Return: height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, height):
        """ sets the height of the rectangle

        Args
            - height: the new height to set

        Returns: nothing
        """

        if type(height) is not int:
            return TypeError('height must be an integer')

        if height < 0:
            return ValueError('height must be >= 0')

        self.__height = height
