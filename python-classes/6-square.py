#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        "Initializes a Square object with a given size"

        self.__size = size
        self.__position = position
    
    def __str__(self):
        self.my_print()

    """###################################################"""

    @property
    def size(self):
        """return size of square"""

        return self.__size

    @property
    def position(self):
        """return position of square"""

        return self.__position

    """###################################################"""

    @size.setter
    def size(self, value):
        "set size with value"

        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        "set position with value"

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    """###################################################"""

    def area(self):
        """get the area of a square"""

        return self.__size * self.__size

    def pos_print(self):
        """get the position in spaces"""

        res = ""
        for i in range(self.__position[1]):
            res += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                res += " "
            for k in range(self.size):
                res += "#"
            res += "\n"

        return res

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end="")
