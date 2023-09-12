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

    def to_json(self):
        """Retrieves a dictionary representation of a Student intance

        Returns: the dictionary representing the student
        """

        return self.__dict__
