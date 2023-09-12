#!/usr/bin/python3
"""Module 1-write_file
Writes a string to a file
"""


def write_file(filename="", text=""):
    """writes a string to a file

    Args:
        - filename: name of the file to write to
        - text: the string to write to @filename
    """

    with open(filename, "w") as f:
        return f.write(text)
