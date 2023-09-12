#!/usr/bin/python3
"""Module 2-append_write.py
Appends to the end of a file
"""


def append_write(filename="", text=""):
    """appends content to a file

    Args:
        - filename: the file to append to
        - text: the text to append to the file
    """
    with open(filename, "a") as f:
        return f.write(text)
