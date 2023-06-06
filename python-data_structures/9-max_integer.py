#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    if my_list == None:
        return
    for i in my_list:
        if _max < i:
            _max = i
    return _max
