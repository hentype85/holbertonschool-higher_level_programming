#!/usr/bin/python3
"""class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """get size"""
        return self.__width
    
    @property
    def size(self):
        """get size"""
        return self.__height

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
