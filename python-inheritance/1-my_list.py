#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
