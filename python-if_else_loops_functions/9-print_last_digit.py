#!/usr/bin/python3
def print_last_digit(n):
    if n < 0:
        digit = n % -(10)
        print(-(digit), end="")
    else:
        digit = n % 10
        print(digit, end="")
    if digit < 0:
        digit *= -1
    return (digit)
