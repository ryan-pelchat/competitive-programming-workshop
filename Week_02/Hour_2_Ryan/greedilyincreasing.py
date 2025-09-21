"""
Problem Title: greedilyincreasing
Platform: Kattis
Problem URL: https://open.kattis.com/problems/greedilyincreasing
Difficulty: 1.7 Easy

Author: Ryan Pelchat
Date Solved: 2025-09-15
Language: Python3

Approach:
    - strategy
        - Read the input sequence once from left to right.
        - Maintain the last chosen number (`previousNumber`).
        - If the current number is strictly greater than the last chosen,
          append it to the subsequence and update `previousNumber`.
        - At the end, print the length of the subsequence and its elements.
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
"""

import sys

lines = sys.stdin.read().strip().splitlines()
output = []
tempSequence = []
previousNumber = float("-inf")

for number in lines[1].split():
    if int(number) > previousNumber:
        tempSequence.append(number)
        previousNumber = int(number)

output.append(str(len(tempSequence)))
output.append(" ".join(tempSequence))
output.append("\n")
sys.stdout.write("\n".join(output))
