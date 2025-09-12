"""
Problem Title: stockprices
Platform: Kattis
Problem URL: https://open.kattis.com/problems/stockprices
Difficulty: 2.0 Easy
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-11
Language: Python3

Approach:
    - strategy
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: 0(...)
Space Complexity: 0(...)

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...

"""

import sys
import heapq

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()
testCases = int(lines[0])

buyHeap = []
sellHeap = []
output = []

for line in lines:
    if len(lines) != 1:
        tempData = line.split()
        if tempData[0] == "buy":
            heapq.heappush(
                buyHeap,
            )


# strat
# make a buy max heap
# make a sell min heap
