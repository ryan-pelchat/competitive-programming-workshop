"""
Problem Title: Black Friday
Platform: Kattis
Problem URL: https://open.kattis.com/problems/blackfriday
Difficulty: 1.8 Easy
Categories: 3.2 b. Iterative (Two Nested Loops)

Author: Ryan Pelchat
Date Solved: 2025-09-29
Language: Python3

Approach:
    - strategy
        - Count how many players rolled each die value.
        - Iterate from the highest die value (6) down to the lowest (1) and check if
          exactly one player rolled that value. If so, that player wins.
        - If no such value exists, print "none".
    - technique (two pointers, recursion, BFS, etc...)
        - Frequency counting using a dictionary
        - Iterative Search
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
"""

import sys

lines = sys.stdin.read().strip().splitlines()

groupSize = int(lines[0])
players = list(map(int, lines[1].split()))

counts = {}
for i in range(1, 7):
    counts[i] = []

for player, result in enumerate(players):
    counts[result].append(player)

for results in range(6, 0, -1):
    if len(counts[results]) == 1:
        print(counts[results][0] + 1)
        quit()
print("none")
