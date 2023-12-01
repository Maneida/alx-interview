#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island represented by the given grid.

    Args:
    - grid (list of list): A 2D grid representing the island,
      where 1 indicates land and 0 indicates water.

    Returns:
    - int: The perimeter of the island.
    """
    if not grid or not grid[0] or len(grid) > 100 or len(grid[0]) > 100:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
