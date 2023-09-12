#!/usr/bin/python3
"""Module 2-append_write.py
Appends to the end of a file
"""


def append_write(filename="", text=""):
    with open(filename, "a") as f:
        return f.write(text)
