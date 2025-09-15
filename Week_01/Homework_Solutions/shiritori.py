"""
Problem Title: shiritori
Platform: Kattis
Problem URL: https://open.kattis.com/problems/shiritori
Difficulty: 2.3 Easy
Categories:

Author: Ryan Pelchat
Date Solved:
Language: Python3

Approach:
    - strategy
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(...)
Space Complexity: O(...)

Notes:
"""

import sys

lines = sys.stdin.read().splitlines()

usedWords = set()
player = 1  # player 1 is 0 and player 2 is 1

# Initialise the first play
lastUsedWord = lines[1]
usedWords.add(lines[1])

for word in lines[2:]:
    if word in usedWords or word[-1] != lastUsedWord[-1]:
        sys.stdout.write(f"Player {player + 1} lost")
    else:
        player ^= 1

sys.stdout.write("Fair Game")
