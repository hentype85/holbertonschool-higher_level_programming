#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    str = dir(hidden_4)
    for c in str:
        if c[:2] != "__":
            print(c)
