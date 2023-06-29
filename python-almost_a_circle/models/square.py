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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
