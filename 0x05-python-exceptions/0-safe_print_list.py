#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0

    if my_list:
        for i in my_list:
            try:
                print(i, end="")
                n += 1
                if n == x:
                    break
            except IndexError:
                break

    if n > 0:
        print("")
    return n
