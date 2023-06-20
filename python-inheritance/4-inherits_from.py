#!/usr/bin/python3
"""return true if the object is an instance
    of a class inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """return true if is instance of a class inherited
        directly or indirectly"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
