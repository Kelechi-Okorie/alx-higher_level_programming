#!/usr/bin/python3
"""5-save_to_json_file module
Write a function that writes an Object to a test file,
Using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    writes an Object to a text file
    using a JSON representation

    Args:
        - my_object: the object to write
        - filename: file to write to

    Returns: nothing
    """

    with open(filename, "w+") as f:
        json.dump(my_obj, f)
