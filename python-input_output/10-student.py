#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """ initialize new student
            with public attribute instance for easy access and modification"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
            If attrs is a list of strings, only attribute names contained in
            this list must be retrieved """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for a in attrs:
                if hasattr(self, a):
                    json_dict[a] = getattr(self, a)
            return json_dict
