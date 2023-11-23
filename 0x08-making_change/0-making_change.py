#!/usr/bin/python3
"""
Module for make change function
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given total amount.

    :param coins: List of coin values.
    :param total: The total amount to be achieved.
    :return: Fewest number of coins needed. If total is 0 or less, return 0.
             If total cannot be met, return -1.
    """
    if total <= 0:
        return 0

    max_coins = total + 1
    dp = [max_coins] * (total + 1)

    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == max_coins:
        return -1
    else:
        return dp[total]
