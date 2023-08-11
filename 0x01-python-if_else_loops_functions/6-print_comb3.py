#!/usr/bin/python3
for i in range(0, 99):
    if i == 89:
        print(i)
    else:
        if (i // 10) < i % 10:
            print("{:02d}".format(i), end=", ")
