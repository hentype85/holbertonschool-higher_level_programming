#!/usr/bin/python3
"divides all elements of a matrix"


def matrix_divided(matrix, div):
    "divides all elements of a matrix"

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "div must be a number"
    err3 = "division by zero"
    err4 = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError(err2)
    if div == 0:
        raise ZeroDivisionError(err3)

    rowLen = len(matrix[0])

    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(err1)

    newM = []
    for row in matrix:
        newlist = []
        for i in row:
            newlist.append(round((i / div), 2))
        newM.append(newlist)

    if len(row) != rowLen:
        raise TypeError(err4)

    return newM
