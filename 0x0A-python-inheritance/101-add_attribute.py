#!/usr/bin/python3
"""Module 101-add_attribute
function that adds an attribute to an object
"""


def add_attribute(my_obj, my_attr, my_value):
    """Adds an attribute with value can be added

    Args:
        - my_obj: object to add attribute to
        - attr: the attribute to add
        - value: the value of the attribute
    """

    if not hasattr(my_obj, '__slots_') and not hasattr(my_obj, '__dict__'):
        raise TypeError("can't add new attribte")
    if hasattr(my_obj, '__slots__') and not hasattr(my_obj, my_attr):
        raise TypeError("can't add new attribute")

    setattr(my_obj, my_attr, my_value)
