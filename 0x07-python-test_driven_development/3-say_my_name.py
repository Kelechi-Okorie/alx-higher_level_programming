#!/usr/bin/python3
"""
module say_my_name
prints my name
"""


def say_my_name(first_name, last_name=""):
    """says my name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", end="")
    if len(first_name) > 0:
        print(end=" ")
    print(first_name, end="")
    if len(last_name) > 0:
        print(end=" ")
    print(last_name, end="")
