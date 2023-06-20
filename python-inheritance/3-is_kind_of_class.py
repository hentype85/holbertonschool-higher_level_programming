#!/usr/bin/python3
"""check if object is an instance of a classs or an inherited class"""


def is_kind_of_class(obj, a_class):
    """return true if object is an instance of a class that inheridet"""
    return isinstance(obj, a_class)
