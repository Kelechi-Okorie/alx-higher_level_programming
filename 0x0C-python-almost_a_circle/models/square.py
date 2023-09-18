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

        s = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

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

    def update(self, *args, **kwargs):
        """ Updates the attributes of the square

        Args:
         - id: id of the instance
         - size: size of the square
         - x: x position of the square
         - y: y position of the square
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representatio of square"""

        s_dict = {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
        }

        return s_dict
