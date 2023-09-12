#!/usr/bin/python3
"""Module 6-load_from_json_file
creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """loads a python object from a
    JSON file

    Args:
        - filename: the file to load from

    Returns: Python object deserialized from
    a json file
    """

    with open(filename, "r") as f:
        return json.load(f)
