#!/usr/bin/python3
"""class Base"""

import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        fileName = "{}.json".format(cls.__name__)
        if list_objs is None:
            return []
        else:
            jList = []
            for obj in list_objs:
                jList.append(obj.to_dictionary())
            with open(fileName, mode="w", encoding="UTF-8") as fd:
                fd.write(cls.to_json_string(jList))
