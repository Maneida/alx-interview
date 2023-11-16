#!/usr/bin/python3
"""
Module to Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Parameters:
    - matrix: The input matrix to be rotated. Must be a square matrix.

    Do not return anything. The matrix is edited in-place.
    """
    if matrix is None:
        raise Exception
    
    row_len = len(matrix[0])
    column_len = len(matrix)

    n = len(matrix)

    if row_len == column_len and n >= 1:
        # transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                (matrix[j][i], matrix[i][j]) = (matrix[i][j], matrix[j][i])

        # swap columns
        for k in matrix:
            k.reverse()
