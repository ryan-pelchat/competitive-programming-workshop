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

Python only supports min heaps, so to get a max heap, we insert the
numbers as negatives
"""

import sys
import heapq

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()

buyHeap = []
sellHeap = []
output = []

for line in lines:
    lastTransaction = "-"
    outputLine = ""

    # if the next line is a test case or not
    if not line.isdigit():
        order = line.split()  # extract data
        if order[0] == "buy":
            heapq.heappush(buyHeap, [-int(order[4]), int(order[1])])
        else:
            heapq.heappush(sellHeap, [int(order[4]), int(order[1])])

        # if buy and sell are not empty and top of buy >= top of sell
        while buyHeap and sellHeap and (abs(buyHeap[0][0]) >= sellHeap[0][0]):

            traded = min(buyHeap[0][1], sellHeap[0][1])

            buyHeap[0][1] -= traded
            sellHeap[0][1] -= traded

            if buyHeap and buyHeap[0][1] == 0:
                heapq.heappop(buyHeap)
            if sellHeap and sellHeap[0][1] == 0:
                heapq.heappop(sellHeap)

            lastTransaction = str(sellHeap[0][0])

        outputLine += str(sellHeap[0][0]) + " " if sellHeap else "- "
        outputLine += str(-1 * buyHeap[0][0]) + " " if buyHeap else "- "
        outputLine += str(lastTransaction)
        output.append(outputLine)
    else:
        # we are in a new test case, so reset
        buyHeap = []
        sellHeap = []

sys.stdout.write("\n".join(output))

# strat
# make a buy max heap
# make a sell min heap
