#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len = len(sys.argv)
    result = 0
    for i in range(1, len):
        result += int(sys.argv[i])

    print(result)
