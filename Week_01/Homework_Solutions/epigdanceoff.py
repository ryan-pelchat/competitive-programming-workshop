"""
Problem Title: epicdanceoff
Platform: Kattis
Problem URL: https://open.kattis.com/problems/epigdanceoff
Difficulty: 1.9 Easy
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-11
Language: Python3

Approach:
    - strategy
        - Transposed 2D array
        - Iterated through 2D array
            - If it has $ then it is not a delimeter
            - If it doesn't have $ then add 1 to count (new dance move)
    - technique (two pointers, recursion, BFS, etc...)
        - Complete Search
    - why did you choose it?
    - edge cases considered?

Time Complexity: 0(m*n)
    - Each of the m·n characters is visited once (during transpose and scan).
Space Complexity: 0(m*n)
    - The transpose creates a new list of n tuples of length m.

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...

Transpose is O(m * n) complexity, it is the same as a double for loop.
I could have done a double for loop but I found it a bit more fun if
I transposed the 2D array.

I could have also saved space by not creating a new "transpose" list and
just used the "lines" variable with a double for loop. Then the space
complexity would just be O(1).

[*zip(*A)]
*A — unpacking
    In Python, * in a function call unpacks an iterable into separate arguments.
Ex:
    A = [[1, 2, 3], [4, 5, 6]]
    zip(*A)
Is same as:
    zip([1, 2, 3], [4, 5, 6])

zip
    zip takes multiple iterables and groups their elements position by position.
Ex:
    zip([1,2,3], [4,5,6])
    # → (1,4), (2,5), (3,6)

So zip(*A) produces an iterator of tuples that represent the transpose.
"""

import sys

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()
transpose = [*zip(*lines[1:])]  # check notes above for explanation
count = 1
for line in transpose:
    if "$" not in line:
        count += 1
sys.stdout.write(str(count))
