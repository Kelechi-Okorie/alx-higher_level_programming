#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for r in matrix:
            n = len(r) - 1
            i = 0

            while i <= n:
                if i == n:
                    print("{:d}".format(r[i]), end="\n")
                else:
                    print("{:d}".format(r[i]), end=", ")

                i += 1
    else:
        print("".format(), end="\n")
