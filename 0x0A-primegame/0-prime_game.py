#!/usr/bin/python3
"""
Prime Game Module
"""
from typing import List, Optional


def isWinner(x: int, nums: List[int]) -> Optional[str]:
    """
     Determine the winner of a prime game.

    Args:
        x (int): The number of rounds.
        nums (List[int]): An array of n for each round.

    Returns:
        Optional[str]: The name of the player that won the most rounds.
                       If the winner cannot be determined, returns None.
    """
    def is_prime(num):
        """ Function to check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        """ Gets prime numbers up to n """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        """ plays a round of the prime game """
        primes = get_primes_up_to_n(n)
        player = "Maria"

        while n > 1:
            move = 0
            for prime in primes:
                if prime <= n:
                    move = prime
                else:
                    break

            n -= move
            primes = [p for p in primes if p % move != 0]

            if player == "Maria":
                player = "Ben"
            else:
                player = "Maria"

        return player

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        winner = play_round(nums[i])
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
