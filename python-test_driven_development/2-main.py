#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [3, 6, 9],
    [12, 15, 18]
]

print(matrix_divided(matrix, 3))
print(matrix_divided(matrix2, 3))
print(matrix_divided(None, 3))
print(matrix)
