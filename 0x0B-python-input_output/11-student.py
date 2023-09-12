#!/usr/bin/python3
"""Module 9-student
Defines a student class with some attributes
"""


class Student:
    """The student class
    Public attributes:
        - first_name
        - last_name
        -age
    Public method to_json()
    """

    def __init__(self, first_name, last_name, age):
        """The student object constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student intance

        Arg:
            - attrs: list of attributes to retrieve

        Returns: List of attributes contained in attrs, if attrs is not None
        otherwise retrieve all attributes
        """

        my_dict = dict()
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            for attr in attrs:
                if attr in self.__dict__:
                    my_dict.update({attr: self.__dict__[attr]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of student instance

        Args:
            - json: dictionary of attributes

        Returns: nothing
        """

        for attrib in json:
            self.__dict__.update({attrib: json[attrib]})
