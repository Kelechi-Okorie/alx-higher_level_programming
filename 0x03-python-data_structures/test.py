#!/usr/bin/python3

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

for r in matrix:
    n = len(r) - 1
    i = 0

    while i <= n:
        if i == n:
            print("{:d}".format(r[i]), end="\n")
        else:
            print("{:d}".format(r[i]), end=", ")

        i += 1


