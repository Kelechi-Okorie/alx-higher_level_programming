#!/usr/bin/python3

def uniq_add(my_list=[]):
    acc = 0
    if my_list:
        for i in list(set(my_list)):
            acc += i

    return acc
