#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Returns the result of multiplying
    two matrices
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for r in m_a:
        for c in r:
            if type(c) is not int and type(c) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for r in m_b:
        for c in r:
            if type(c) is not int and type(c) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_len = []
    for r in m_a:
        row_len.append(len(r))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_a must be of the same size")
    row_len = []
    for r in m_b:
        row_len.append(len(r))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_b must be of same size")

    a_col = 0
    for col in m_a[0]:
        a_col += 1
    b_row = 0
    for row in m_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
