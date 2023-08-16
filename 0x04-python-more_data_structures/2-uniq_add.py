#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        acc = 0
        for i in list(set(my_list)):
            acc += i

        return acc
