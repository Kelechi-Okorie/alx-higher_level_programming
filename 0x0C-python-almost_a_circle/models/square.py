#!/usr/bin/python3
"""module square
Inherits from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class
    Inherits from from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the square instance

        Args:
            - size: size of the square
            - x: x position of the square
            - y: y position of the square
            - id: id of the square

        Returns: None
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The __str__ function for printing
        the square instance

        Returns: None
        """

        s = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

        return s
    
    @property
    def size(self):
        """Returns the size attribute of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the size attribute of the square"""

        self.width = size
        self.height = size
