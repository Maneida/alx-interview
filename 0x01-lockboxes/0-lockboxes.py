#!/usr/bin/python3
"""
Defines a function canUnlockAll to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened and
    returns True if all boxes can be opened, else False
    """
    if not boxes:
        return False

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
