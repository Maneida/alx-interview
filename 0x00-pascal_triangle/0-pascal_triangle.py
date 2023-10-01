#!/usr/bin/python3
"""
Pascal triangle technical interview test
"""


def pascal_triangle(n):
    """Returns list of lists of integers representing the Pascal triangle of n

    Args:
        n (int): number of levels of the Pascal's triangle
    """
    if not n > 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            val = triangle[i - 1][j - 1] + triangle[i-1][j]
            row.append(val)
        row.append(1)
        triangle.append(row)

    return triangle
