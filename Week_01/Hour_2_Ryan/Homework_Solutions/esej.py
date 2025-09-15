"""
Problem Title: esej
Platform: Kattis
Problem URL: https://open.kattis.com/problems/esej
Difficulty: 3.4 Medium
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-14
Language: Python3

Approach:
    - strategy
        - Output must satisfy 3 conditions:
        1. Contains at least A words and at most B words
            - Always output B words
        2. Every word contains at least one, and at most 15 letters
            - Satisfied through step 3
        3. contains at least B/2 different words.
            - In the worse case we need 50 000 new words
            - Count up from 1 till B, and numbers 1-10 are assigned to a
              unique letter.
            - This build a unique word for up to 10^14 unique words
              (a number of length 14)
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?
        - the word count cannot always be A (it fails otherwise)

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...

https://stackoverflow.com/a/71680813
"""

import sys

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
line = sys.stdin.read().split()
a = int(line[0])
b = int(line[1])
output = []
alphabet = "qwertyuiop"  # only 10 characters needed
counter = 1

for i in range(b):
    newWord = ""
    # build the new word
    for letter in str(counter):
        newWord += alphabet[int(letter)]

    counter += 1

    output.append(newWord)
sys.stdout.write(" ".join(output))
