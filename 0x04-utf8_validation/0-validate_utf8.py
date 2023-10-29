#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Validates if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers representing 1-num data.

    Returns:
        bool: True for valid UTF-8, else False.
    """
    expected_bytes = 0

    for num in data:
        if expected_bytes == 0:
            if num >> 7 == 0b0:
                continue
            elif num >> 5 == 0b110:
                expected_bytes = 1
            elif num >> 4 == 0b1110:
                expected_bytes = 2
            elif num >> 3 == 0b11110:
                expected_bytes = 3
            else:
                return False
        else:
            if num >> 6 == 0b10:
                expected_bytes -= 1
            else:
                return False

    return expected_bytes == 0
