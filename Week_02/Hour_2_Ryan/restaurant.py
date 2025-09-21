"""
Problem Title: restaurant
Platform: Kattis
Problem URL: https://open.kattis.com/problems/restaurant
Difficulty: 3.1 Medium

Author: Ryan Pelchat
Date Solved: 2025-09-18
Language: Python3

Approach:
    - strategy
        - Always DROP everything into stack 2.
        - TAKE from stack 1, if not enough:
            - If stack1 > 0: take what's there
            - Move everything from stack2 to stack1
              then take the remaining from stack1
    - technique (two pointers, recursion, BFS, etc...)
        - simulation of stack operations
        - Greedy strategy, always DROP to stack2, always TAKE from
          stack1 when possible.
    - why did you choose it?
    - edge cases considered?
        - Ensuring not to do operations on empty stacks
        - Ensuring to ignore input ending with 0

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
"""

import sys
from typing import *

lines = sys.stdin.read().strip().splitlines()

output = []

stack1 = 0
stack2 = 0

for line in lines[1:]:
    values = line.split()
    if line.isdigit():
        output.append("")
        stack1 = 0
        stack2 = 0
    else:
        operation = values[0]
        plates = int(values[1])
        if operation == "DROP":
            # always drop off in stack2
            stack2 += plates
            output.append(f"DROP 2 {plates}")
        else:  # must be that values[0] == "TAKE"
            # if stack1 has enough then take from stack1
            if stack1 >= plates:
                output.append(f"TAKE 1 {plates}")
                stack1 -= plates
            else:
                # take what's left in stack 1 (if any)
                if stack1:
                    output.append(f"TAKE 1 {stack1}")
                    plates -= stack1
                    stack1 = 0
                # move everything from 2 -> 1 (if any)
                if stack2:
                    output.append(f"MOVE 2->1 {stack2}")
                    stack1 += stack2
                    stack2 = 0
                # now take the remainder from stack 1
                stack1 -= plates
                output.append(f"TAKE 1 {plates}")

sys.stdout.write("\n".join(output))
