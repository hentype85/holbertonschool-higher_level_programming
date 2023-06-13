#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square object"""

    def __init__(self, size=0, position=(0, 0)):
        "Initializes a Square"

        if type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @property
    def position(self):
        """get position"""
        return self.__position

    @size.setter
    def size(self, value):
        "set size"
        self.__size = value

    @position.setter
    def position(self, value):
        "set position"
        self.__position = value

    def area(self):
        """area of a square"""
        return self.__size ** 2

    def my_print(self):
        """draw the square"""
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")

            for k in range(self.__size):
                print("#", end="")

            print()
