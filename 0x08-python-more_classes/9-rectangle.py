#!/usr/bin/python3
""" Rectangle class bases on 0-rectangle.py """


class Rectangle:
    """ Rectangle class bases on 0-rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor for rectangle class

        Args:
            - wdith: with of the rectangle instance
            - height: height of the rectangle instance

        Returns: Nothing
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

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
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height

    def area(self):
        """ Calculates and returns the area of the rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ Calculates and returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ returns the string representation of the rectangle """

        string = ""

        if self.__width == 0 or self.__height == 0:
            return string

        for h in range(0, self.__height):
            for w in range(0, self.__width):
                string = string + str(self.print_symbol)
            string = string + "\n"

        return string[:-1]

    def __repr__(self):
        """ returns a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle by computing area
        of rect_1 and rect_2

        Args:
            - rect_1: rectangle 1
            - rect_2: rectangle 2

        Returns: the bigger of the rectangles
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new rectangle with width == height == size

        Args:
            - size: size of the square

        Returns: a new rectangle with width == height == size
        """

        return cls(size, size)

    def __del__(self):
        """ The destructor for Rectangle class """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
