#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """prints content of UTF8 text file"""
    with open(filename, encoding="UTF-8") as fd:
        print(fd.read(), end="")
