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
        fileName = cls.__name__ + ".json"
        with open(fileName, mode="w") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                jList = []
                for obj in list_objs:
                    jList.append(obj.to_dictionary())
                fd.write(cls.to_json_string(jList))
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
