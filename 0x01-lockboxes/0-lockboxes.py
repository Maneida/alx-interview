#!/usr/bin/python3
"""
Defines a function canUnlockAll to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened and
    returns True if all boxes can be opened, else False
    """
    if type(boxes) is not list:
        raise TypeError("Input must be a list.")

    for box in boxes:
        if type(box) is not list:
            raise TypeError("Each element in the list must be a list.")

    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box, which is unlocked

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if not visited[key]:
                stack.append(key)

    return all(visited)
