#!/usr/bin/python3
"""Module 4-free_json_string
returns an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """from_json_string function

    Returns the object (Python data structure) represented by a JSON string

    Args:
        - my_str: the json string to deserialize

    Returns: the deserialized python object
    """

    return json.loads(my_str)
