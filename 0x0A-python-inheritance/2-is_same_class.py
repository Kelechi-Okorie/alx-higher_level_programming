#!/usr/bin/python3
"""Module 2-is_same_class
Checks if an object is an instance of a given class
"""


def is_same_class(obj, a_class):
    """Function that determins if obj is an instance of a_class

    Args:
        - obj: the object to check
        - a_class: the class to check instance of

    Returns: True if obj is an instance of a_class,
    False otherwise
    """

    return True if type(obj) is a_class else False
