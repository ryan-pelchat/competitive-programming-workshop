"""
Problem Title: Teque
Platform: Kattis
Problem URL: https://open.kattis.com/problems/teque
Difficulty: 3.2 Medium

Author: Ryan Pelchat
Date Solved: 2025-09-21
Language: Python3

Approach:
    - strategy
        - Invariant:
            - len(q1) == len(q2) + 1 || len(q1) == len(q2)
        - Use 2 double ended queues
        - Keep both queues balanced so the middle stays the middle
    - technique (two pointers, recursion, BFS, etc...)
        - used 2 double ended queues
    - why did you choose it?
    - edge cases considered?
        - The new index for x in a push_middle is (k+1)/2 if k is an odd
          number, otherwise it is just the middle (0 based indexing)
        - After push back and push front, you need to rebalance if
          necessary to keep the invariant true

Time Complexity: O(n)
    - all is O(1) but get operations which is O(n)
        - "Indexed access is O(1) at both ends but slows to O(n) in the middle."
        - https://docs.python.org/3/library/collections.html#collections.deque.maxlen
Space Complexity: O(n)

Notes:
Ch 2.2 problem l. List/Queue/Deque
"""

import sys
from collections import deque


def rebalance(q1: deque, q2: deque) -> None:
    """
    Maintains invariant:
        len(q1) == len(q2) + 1 || len(q1) == len(q2)
    Moves 1 element across if violated

    Returns None, modifies the deques.
    """
    if len(q1) < len(q2):
        q1.append(q2.popleft())
    elif len(q2) + 1 < len(q1):
        q2.appendleft(q1.pop())


lines = sys.stdin.read().strip().splitlines()

commands = lines[1:]

q1 = deque()
q2 = deque()

output = []

for command in commands:
    parsedCommand = command.split()
    op, x = parsedCommand[0], int(parsedCommand[1])

    if op == "push_back":
        q2.append(x)
        rebalance(q1, q2)
    elif op == "push_front":
        q1.appendleft(x)
        rebalance(q1, q2)
    elif op == "push_middle":
        if len(q2) < len(q1):
            q2.appendleft(x)
        else:
            # if q1 is smaller or equal to q2
            # this default behaviour is needed to comply with the new
            # insertion index of x being (k+1)/2
            q1.append(x)
    else:
        # operation must be "get"
        if x < len(q1):
            output.append(str(q1[x]))
        else:
            output.append(str(q2[x - len(q1)]))

sys.stdout.write("\n".join(output))
