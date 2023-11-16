#!/usr/bin/python3
"""
Module to Rotate 2D Matrix
"""
from typing import List

def rotate_2d_matrix(matrix: List[List]) -> List[List]:
    """ rotates matrix clockwise """
    row_len = len(matrix[0])
    column_len = len(matrix)

    if row_len == column_len:
        matrix[0][0] = 5
        # transpose matrix

        #swap columns

        
    return matrix