#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        if (ord(s) >= 97 and ord(s) <= 122):
            s = chr(ord(s) - 32)
        print(f"{s}", end="")
    print("")
