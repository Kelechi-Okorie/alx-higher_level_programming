#!/usr/bin/python3
"""Module inherits_from
Checks if object is an instance of a class that inherited
(directoy or indirectory) from a specified class
"""


def inherits_from(obj, a_class):
    """checks if obj is a direct descendant of a_class

    Args:
        - obj: the object to check
        - a_class: the class to compare with

    Returns: True if obj is a descendant of a_class, False otherwise
    """

    return isinstance(obj, a_class) and not (type(obj) is a_class)
