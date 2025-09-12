"""
Problem Title: jollyjumpers
Platform: Kattis
Problem URL: https://open.kattis.com/problems/jollyjumpers
Difficulty: 2.5 Easy
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-11
Language: Python3

Approach:
    - strategy
        - Iterative Search
        - Used bitmask as a set
        - To be Jolly, absolute differences of successive elements must
          be exactly the set {1..n−1}
            - We can get 3 things out of this
                1. if there are duplicate numbers, then Not Jolly
                2. if numbers are outside of range, then Not Jolly
                3. if ~1 ^ ~2 => Jolly (if not 1 and 2 then Jolly)
    - technique (two pointers, recursion, BFS, etc...)
        - Complete Search with pruning
    - why did you choose it?
    - edge cases considered?
        - difference is 0

Time Complexity: 0(n)
Space Complexity: 0(1)
    - The input is a given
    - Other variables are scalar

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...
"""

import sys

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()

for line in lines:
    numbers = list(map(int, line.split()))
    n = numbers[0]
    isJolly = None
    mask = 0  # create a bitmask to use as a set

    for i in range(2, n):
        testNum = abs(numbers[i] - numbers[i - 1])
        # checks if testNum in mask already
        if mask & (1 << testNum) > 0 or testNum >= n or testNum == 0:
            sys.stdout.write("Not jolly\n")
            isJolly = False
            break
        else:
            # adds testNum to mask
            mask |= 1 << testNum

    if isJolly is None:
        sys.stdout.write("Jolly\n")
