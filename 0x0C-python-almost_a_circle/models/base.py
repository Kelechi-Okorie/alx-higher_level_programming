#!/usr/bin/python3
"""Model base
This is the base of all other classes in the project
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON representation of list_dictionaries

        Args
            - list_dictionaries: list of dictionaries

        Returns: JSON representation of the list
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        if (type(list_dictionaries) is not list or
                not all(type(x) is dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        return json.dumps(list_dictionaries)
