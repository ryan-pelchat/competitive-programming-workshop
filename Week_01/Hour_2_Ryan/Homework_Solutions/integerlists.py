"""
Problem Title: integerlists
Platform: Kattis
Problem URL: https://open.kattis.com/problems/integerlists
Difficulty: Medium 3.2
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-11
Language: Python3

Approach:
    - strategy
        - Use a deque to simulate deletions efficiently from both ends
          while tracking orientation.
    - technique (two pointers, recursion, BFS, etc...)
        - deque
        - simulation
        - Complete Search
    - why did you choose it?
        - Because deque gives O(1) pops from both ends, unlike list.
    - edge cases considered?

Time Complexity: 0(n)
Space Complexity: 0(n)

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...
"""

import sys
from collections import deque

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()
out = []  # buffer output first

for i in range(int(lines[0])):

    bapc = lines[i * 3 + 1]  # every 3 newlines, new BAPC program

    data = lines[i * 3 + 3]
    innerData = data[1:-1]  # to remove brackets

    dq = deque() if innerData == "" else deque(innerData.split(","))

    forward = True  # True is forward, False is backwards
    error = False

    for command in bapc:
        if command == "R":
            forward = not forward
        else:  # then it is "D"
            if not dq:  # checking if dq is empty
                out.append("error")
                error = True
                break
            if forward:
                dq.popleft()
            else:
                dq.pop()

    if not error:
        if forward:  # if even then no change
            out.append("[" + ",".join(dq) + "]")
        else:
            # if odd then need to reverse list before printing
            out.append("[" + ",".join(reversed(dq)) + "]")

sys.stdout.write("\n".join(out))  # write in one go
