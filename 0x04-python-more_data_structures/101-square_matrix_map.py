#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda r: [r[0] * r[0], r[1] * r[1], r[2] * r[2]], matrix))
