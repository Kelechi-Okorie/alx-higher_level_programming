#!/usr/bin/python3
"""Module 8-class_to_json
Returns the dictionary description with
with simple data sttructures
"""


def class_to_json(obj):
    """returns a dictionary description of obj

    Arg:
        - obj: the object to return dictionary of

    Returns: dictionary representation of obj
    """

    return obj.__dict__
