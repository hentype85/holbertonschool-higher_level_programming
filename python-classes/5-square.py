#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        "Initializes a Square object with a given size"

        self.__size = size

    @property
    def size(self):
        """return size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        "set size with value"

        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
