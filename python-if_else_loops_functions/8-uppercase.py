#!/usr/bin/python3
def uppercase(_c):
    for i in _c:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(f"{i}", end="")
    print()
