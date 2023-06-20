#!/usr/bin/python3
"""Rectangle subclass Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """class to define square inherits from BaseGeometry"""

    def __init__(self, size):
        """intialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
