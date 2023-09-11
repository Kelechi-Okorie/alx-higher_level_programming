#!/usr/bin/python3
"""Module 101-add_attribute
functio that adds an attribute to an object
"""


def add_attribute(my_obj, attr, value):
    """Adds an attribute if it can be added

    Args:
        - my_obj: object to add attribute to
        - attr: the attribute to add
        - value: the value of the attribute
    """

    if not hasattr(my_obj, '__slots_') and not hasattr(my_obj, '__dict__'):
        raise TypeError("can't add new attribte")
    if hasattr(my_obj, '__slots__') and not hasattr(my_obj, attr):
        raise TypeError("can't add new attribute")

    setattr(my_obj, attr, value)
