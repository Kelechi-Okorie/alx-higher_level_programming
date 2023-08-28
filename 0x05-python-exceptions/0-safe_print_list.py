#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0

    for i in my_list:
        if n == x:
            break
        try:
            print(i, end="")
            n += 1
        except IndexError:
            pass

    print()
    return n
