#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        weighted_sum = 0
        total_weight = 0

        for i in my_list:
            weighted_sum += i[0] * i[1]
            total_weight += i[1]

        return weighted_sum / total_weight

    return 0
