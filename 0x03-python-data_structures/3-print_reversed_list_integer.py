#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if (len(my_list) == 0):
        return None

    list_len = len(my_list) - 1

    while list_len >= 0:
        print("{:d}".format(my_list[list_len]))
        list_len -= 1
