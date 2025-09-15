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
    - technique (two pointers, recursion, BFS, etc...)
        - Hash Table to keep count
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...
"""

import sys
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

maxVotes = max(dic.values())
# only adds name if the corresponding v is equal to maxVotes
winner = [name for name, v in dic.items() if v == maxVotes]

if len(winner) > 1:
    sys.stdout.write("Runoff!")
else:
    sys.stdout.write(f"{winner[0]}\n")
