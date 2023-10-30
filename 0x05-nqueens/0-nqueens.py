#!/usr/bin/python3
"""
Nqueens module
"""
import sys


def nqueens() -> None:
    """ Nqueens puzzle function representation """

    try:
        N = int(sys.argv[1])
        if N < 4:
            pass
        print("hello")

        # add all function logic here

    except ValueError as e:
        print("Usage: nqueens N")


if __name__ == "__main__":
    nqueens()
