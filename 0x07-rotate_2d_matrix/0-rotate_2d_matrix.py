#!/usr/bin/python3
"""
Module to Rotate 2D Matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    """ rotates matrix clockwise """
    row_len = len(matrix[0])
    column_len = len(matrix)

    if row_len == column_len:
        n = len(matrix)

        # transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                (matrix[j][i], matrix[i][j]) = (matrix[i][j], matrix[j][i])

        # swap columns
        for k in range(n):
            matrix[k].reverse()
