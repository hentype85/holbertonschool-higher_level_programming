#!/usr/bin/python3
"divides all elements of a matrix"


def matrix_divided(matrix, div):

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "div must be a number"
    msg3 = "division by zero"
    msg4 = "Each row of the matrix must have the same size"

    if type(matrix) is None or type(matrix) != list:
        raise TypeError(msg1)
    if type(div) != int and type(div) != float:
        raise TypeError(msg2)
    if div == 0:
        raise ZeroDivisionError(msg3)

    rowLen = len(matrix[0])

    for row in matrix:
        if len(row) != rowLen:
            raise TypeError(msg4)

    newM = []
    for col in matrix:
        newlist = []
        for row in col:
            newlist.append(round((row / div), 2))
        newM.append(newlist)

    return newM
