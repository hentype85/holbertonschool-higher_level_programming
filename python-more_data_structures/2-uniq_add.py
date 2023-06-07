#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    num = 0
    for i in my_list:
        if i not in newlist:
            newlist.append(i)
            num += i
    return num
