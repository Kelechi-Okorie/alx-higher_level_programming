#!/usr/bin/python3
"""Model base
This is the base of all other classes in the project
"""


class Base:
    """The Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor for Base class

        Args:
            - id: id of the current instance

        Returns: none
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
