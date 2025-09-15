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
        - Simulate the game, use a set to see if a word was used before
        - Used a bit and flipped it to keep track of player turns
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
"""

import sys

lines = sys.stdin.read().splitlines()

usedWords = set()
player = 1  # player 1 is 0 and player 2 is 1

# Initialise the first play
lastUsedWord = lines[1]
usedWords.add(lines[1])

loseFlag = False

for word in lines[2:]:
    if word in usedWords or word[0] != lastUsedWord[-1]:
        sys.stdout.write(f"Player {player + 1} lost")
        loseFlag = True
        break
    else:
        player ^= 1
        lastUsedWord = word
        usedWords.add(word)

if not loseFlag:
    sys.stdout.write("Fair Game")
