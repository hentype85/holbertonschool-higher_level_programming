#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newM = []
    for i in matrix:
        _power = []
        for j in i:
            _power.append(j ** 2)
        newM.append(_power)
    return (newM)
