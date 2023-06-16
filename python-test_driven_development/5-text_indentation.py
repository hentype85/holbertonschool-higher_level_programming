#!/usr/bin/python3
"""prints a text with 2 new lines after each special char"""


def text_indentation(text):
    """text with 2 new lines after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    specialChar = [".", "?", ":"]
    new = ""
    flag = True

    for char in text:

        if char in specialChar:
            new += char + "\n\n"
            flag = True

        elif flag is True and char == " ":
            continue

        else:
            new += char
            flag = False

    print(new, end="")
