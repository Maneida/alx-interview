#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data: list[int]) -> bool:
    """
    Validates if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers representing 1-byte data.

    Returns:
        bool: True for valid UTF-8, else False.
    """
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 7) == 0b0:
                num_bytes = 0
            else:
                return False
        else:
            if (num >> 6) == 0b10:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
