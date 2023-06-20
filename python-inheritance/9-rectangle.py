#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class to define rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """intialize a new Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ rectangle description: [Rectangle] <width>/<height>"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
