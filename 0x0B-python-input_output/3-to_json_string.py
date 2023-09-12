#!/usr/bin/python3
"""Module 3-to_json_string
Converts objects to their json representation
"""


import json


def to_json_string(my_obj):
    """Converts objects to their json representation

    Arg:
        - my_bj: the object to convert

    Returns: json representation of my_obj
    """

    return json.dumps(my_obj)
