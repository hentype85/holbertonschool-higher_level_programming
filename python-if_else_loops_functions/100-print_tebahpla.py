#!/usr/bin/python3
for _ascii in range(122, 96, -1):
    if (_ascii % 2 == 0):
        print("{}".format(chr(_ascii)), end="")
    else:
        print("{}".format(chr(_ascii - 32)), end="")
