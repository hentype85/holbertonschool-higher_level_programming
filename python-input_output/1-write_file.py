#!/usr/bin/python3
"""writes to a text file (UTF8) and
returns the number of characters written
"""
def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""

    with open(filename, "w",encoding="UTF-8") as fd:
        return fd.write(text)
