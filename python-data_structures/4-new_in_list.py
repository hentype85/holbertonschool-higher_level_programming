#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _copy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return _copy
    else:
        _copy[idx] = element
        return _copy
