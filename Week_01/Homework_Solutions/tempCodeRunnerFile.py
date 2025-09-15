"""
Problem Title: recount
Platform: Kattis
Problem URL: https://open.kattis.com/problems/recount
Difficulty: 2.1 Easy
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-15
Language: Python3

Approach:
    - strategy
        - Used a dictionary to keep track of the count
        - Used a priority heap to find out the winner and if there is a
          non-mahority
    - technique (two pointers, recursion, BFS, etc...)
        - Hash Table to keep count
        - Min Priority Heap to find winner and if there is a non-majority
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(nlogn)
    - I need to push everythin into a heap
Space Complexity: O(n)

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...

Python only supports min heaps, so to get a max heap, we insert the
numbers as negatives
"""

import sys
import heapq
from collections import defaultdict

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()

dic = defaultdict(int)

peopleHeap = []

for line in lines:
    if line != "***":
        dic[line] += 1

for key in list(dic.keys()):
    heapq.heappush(peopleHeap, [-1 * dic[key], key])

maxVotes = max(dic.values())
winner = [name for name, v in dic.items() if v == maxVotes]

if len(winner) > 1:
    sys.stdout.write(f"{heapq.heappop(peopleHeap)[1]}")
else:
    sys.stdout.write(f"{winner[0]}\n")

# if len(peopleHeap) == 1:
#     sys.stdout.write(f"{heapq.heappop(peopleHeap)[1]}")
# else:
#     candidate1 = heapq.heappop(peopleHeap)
#     candidate2 = heapq.heappop(peopleHeap)
#     if candidate1[0] == candidate2[0]:
#         sys.stdout.write("Runoff!")
#     else:
#         sys.stdout.write(f"{candidate1[1]}")
