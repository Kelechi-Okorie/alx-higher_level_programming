#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        return [[c * c for c in r] for r in matrix]
