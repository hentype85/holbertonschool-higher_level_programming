#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square object"""

    def __init__(self, size=0, position=(0, 0)):
        "Initializes a Square object with a given values"
        self.size = size
        self.position = position

    @property
    def size(self):
        """get return size of square"""
        return self.__size

    @property
    def position(self):
        """get return position of square"""
        return self.__position

    @size.setter
    def size(self, value):
        "set size"
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        "set position"
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
