#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0
    if roman_string is None:
        return result

    mappings = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    prev = int(mappings[roman_string[0]])

    for i in roman_string:
        if i not in mappings:
            return result
        val = int(mappings[i])
        if val > prev:
            result = result - prev * 2

        result += val
        prev = val

    return result
