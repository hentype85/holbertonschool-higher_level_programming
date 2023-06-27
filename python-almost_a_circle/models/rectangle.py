#!/usr/bin/python3
"""class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
