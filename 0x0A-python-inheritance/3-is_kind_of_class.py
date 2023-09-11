#!/usr/bin/python3
"""Module is_kind_of
Checks if object is instance of or instance of class
that inherits from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is instance of,
    or instance of class that inherits
    from a_class

    Args:
        - obj: the object to check
        - a_class: the class to compare with
    Returns: True if successful or False otherwise
    """

    return isinstance(obj, a_class)
