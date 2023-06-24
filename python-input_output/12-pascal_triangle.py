#!/usr/bin/python3
""" returns a list of lists of integers
    representing the Pascals triangle of n"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                num = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(num)
            row.append(1)
            triangle.append(row)

        return triangle
