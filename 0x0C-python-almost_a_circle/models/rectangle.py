#!/usr/bin/python3
"""module rectangle
The rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """The rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method for rectangle class

        Args:
            - __width: width of the rectangle
            - __height: height of the rectangle
            - __x: x position of the rectangle
            - __y: y position of the rectangle
            - id: id of the rectangle

        Return: None
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for the width attribute

        Returns: None
        """

        return self.__width

    @width.setter
    def width(self, width):
        """setter for the width attribute

        Args:
            - width: width of the rectangle
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter for the height attribute

        Returns: None
        """

        return self.__height

    @height.setter
    def height(self, height):
        """setter for the height attribute

        Args:
            - height: height of the rectangle
        Returns: None
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for the x attribute

        Returns: None
        """

        return self.__x

    @x.setter
    def x(self, x):
        """setter for the x attribute

        Args:
            -x: x position of the rectangle
        Returns: None
        """

        if type(x) is not int:
            raise TypeError("x must be an int")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for the y attribute

        Rectangle
        """

        return self.__y

    @y.setter
    def y(self, y):
        """setter for the y attribute

        Args:
            -y: y position of the rectangle
        Returns: None
        """

        if type(y) is not int:
            raise TypeError("y must be an int")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the rectangle instance

        Returns: The area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """prints in the stdout the Rectangle instance
        with the character x

        Returns: None
        """

        for y in range(0, self.__y):
            print()

        for h in range(self.__height):
            for x in range(0, self.x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of a
        Rectangle instance
        """

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return s
    
    def update(self, *args):
        """Updates the variables of the rectangle

        Args
            - id: id of the rectangle
            - width: width of the rectangle
            - height: height of the rectangle
            - x: x position of the rectangle
            - y: y position of the rectangle

        Returns: None
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int:
                    raise TypeError("id must be an integer")
                self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                if len(args) > 3:
                    self.x = args[3]
                if len(args) > 4:
                    self.y = args[4]
