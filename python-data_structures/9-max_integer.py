#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = None
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if _max < i:
                _max = i
    return _max
