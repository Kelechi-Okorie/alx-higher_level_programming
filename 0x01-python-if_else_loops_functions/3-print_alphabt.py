#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1, 1):
    if c == 'q' or c == 'e':
        continue
    print("{:c}".format(c), end="")
