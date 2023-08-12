#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    if idx >= len(my_list):
        return my_list

    length = len(my_list)
    i = 0
    new_list = []

    for i in my_list:
        new_list.append(i)

    new_list[idx] = element
    return new_list
