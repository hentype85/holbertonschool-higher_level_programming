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

    def to_json(self):
        """get dictionary containing the student attributes"""
        return self.__dict__
