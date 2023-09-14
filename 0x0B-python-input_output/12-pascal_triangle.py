#!/usr/bin/python3
"""Module 12-pascal_triangle
Builds a pascal triangle
"""


def pascal_triangle(n):
    """Builds and returns a pascal triangle of size n

    Args:
        - n: size of the triangle
    """

    triangle = []

    if n <= 0:
        return triangle

    for i in range(1, n + 1):
        inner = []
        for j in range(1, i + 1):
            if i == 1 or j == i:
                inner.append(1)
                continue
            ci_1 = triangle[i - 2][j - 2]
            ci = triangle[i - 2][j - 1]
            print(ci_1, ci, triangle[i - 2])
            inner.append(ci_1 + ci)
        triangle.append(inner)

    return triangle
