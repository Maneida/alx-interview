#!/usr/bin/python3
"""
Prime Game Module
"""
from typing import List


def getPrimes(n: int) -> tuple:
    """ Gets prime numbers up to n """
    nums = list(range(2, n + 1))
    primes, composites = [], []
    if n < 4:
        return nums, composites

    for num in nums:
        if num < 4:
            primes.append(num)
        else:
            for x in range(2, num + 1):
                if not num % x:
                    composites.append(num) if x != num else primes.append(num)
                    break

    return primes, composites


def isWinner(x: int, nums: list) -> str:
    """
     Determine the winner of a prime game.

    Args:
        x (int): The number of rounds.
        nums (List[int]): An array of n for each round.

    Returns:
        Optional[str]: The name of the player that won the most rounds.
                       If the winner cannot be determined, returns None.
    """
    if not isinstance(x, int) or x <= 0 \
            or not nums or not isinstance(nums, list):
        return None

    winner = 0
    for n in nums[:x]:
        if not isinstance(n, int):
            continue
        primes, composites = getPrimes(n)
        winner += -1 if not len(primes) else -1 if not len(primes) % 2 else 1

    return 'Maria' if winner > 0 else 'Ben' if winner < 0 else None
