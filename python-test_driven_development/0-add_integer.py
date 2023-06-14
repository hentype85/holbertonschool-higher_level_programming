#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    "addition a and b"

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
