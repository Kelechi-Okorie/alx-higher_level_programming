#!/usr/bin/python3
"""Module 0-read_file.py
Reads a file
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
