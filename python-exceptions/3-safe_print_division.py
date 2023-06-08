#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = None
        res = a / b
    except (ZeroDivisionError):
        return res
    else:
        return res
    finally:
        print("Inside result: {}".format(res))
