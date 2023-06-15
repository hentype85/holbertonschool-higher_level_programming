#!/usr/bin/python3
"divides all elements of a matrix"


def matrix_divided(matrix, div):
    if type(matrix) == None or type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    rowLen = len(matrix[0])

    for row in matrix:
        if len(row) != rowLen:
            raise TypeError("Each row of the matrix must have the same size")

    newM = []
    for col in matrix:
        newlist = []
        for row in col:
            newlist.append(round((row / div), 2))
        newM.append(newlist)

    return newM
