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

    for col in matrix:
        for row in col:
            if not isinstance(row, (int, float)):
                raise (err1)

    newM = []
    for col in matrix:
        newlist = []
        for row in col:
            newlist.append(round((row / div), 2))
        newM.append(newlist)

    if len(col) != rowLen:
        raise TypeError(err4)

    return newM
