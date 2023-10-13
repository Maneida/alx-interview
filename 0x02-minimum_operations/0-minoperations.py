#!/usr/bin/python3
""" Minimum Operations Module"""


def minOperations(n: int) -> int:
    """ Minimum Operations Function """
    if n <= 1 or isinstance(n, int) is False:
        return 0
    i = 2
    result = 0
    while i <= n:
        if n % i == 0:
            result += i
            n = n / i
        else:
            i += 1
    return result
