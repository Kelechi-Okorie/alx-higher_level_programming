#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None

    return max(a_dictionary)
