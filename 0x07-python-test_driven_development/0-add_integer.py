#!/usr/bin/python3
"""
Module add_integer
Returns the sum of two integers

"""


def add_integer(a, b=98):
    """On success eturns the sum of a and b,
    if a or b is/are not integers, returns an error
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b    
