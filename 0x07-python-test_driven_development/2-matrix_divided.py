#!/usr/bin/python3
"""
Module matrix_divided
divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div
    rounded to 2 decimal places,
    where div is either an int or a float
    and matrix is a list of list

    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for r in matrix:
        if len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of i ntegers/floats")

        for c in r:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    length_rows = []
    for r in matrix:
        length_rows.append(len(r))
    if not all(length == length_rows[0] for length in length_rows):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(c / div, 2) for c in r] for r in matrix]
