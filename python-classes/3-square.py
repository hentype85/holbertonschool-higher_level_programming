#!/usr/bin/python3
"""class Square that defines a square size"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate area of the square"""

        return (self.__size ** 2)
