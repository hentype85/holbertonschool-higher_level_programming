#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    for i in roman_string:
        if i in d:
            res += d[i]
    return res
