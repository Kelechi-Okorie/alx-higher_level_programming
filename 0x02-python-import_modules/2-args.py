#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    message = "arguments."
    if (len == 2):
        message = "argument:"
    elif len > 2:
        message = "arguments:"

    print(f"{len - 1} {message}")

    for i in range(1, len):
        print(f"{i}: {sys.argv[i]}")
