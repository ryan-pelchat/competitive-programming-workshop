# The solution will be here next week
"""
Problem Title: pairingsocks
Platform: kattis
Problem URL: https://open.kattis.com/problems/pairingsocks
Difficulty:
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-11
Language: Python3

Approach:
    - strategy
        - Note that you do not need to consider the case of moving a sock
          from the auxiliary to the original stack; since doing this
          won't change the order.
        - Use 2 stacks, pop from original to auxiliary, count action
            - if they match, pop both, count action
            - continue to check if they match until they don't
            - when original stack is empty, stop
        - if auxiliary stack is empty then output action count
        - if auxiliary stack is not empty then output impossible
    - technique (two pointers, recursion, BFS, etc...)
        - simulation
        - Complete Search
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
3.2.3 Complete Search Tips #5
For Python users, read all input first upfront before processing them
in-memory and buffer output first before writing them out in one go...

Keep in mind that...
    bool([1]) is True
    bool([]) is False
"""
import sys

# read all first, each new line is a new element is list
# How to end input
# Linux / macOS (bash, zsh, etc.): press Ctrl+D on a new line.
# Windows (cmd, PowerShell): press Ctrl+Z then Enter.
lines = sys.stdin.read().splitlines()
stack1 = lines[1].split()

sockPairs = int(lines[0])
moveCounter = 0
stack2 = []

while stack1:
    stack2.append(stack1.pop())
    moveCounter += 1

    while stack1 and stack2 and stack2[-1] == stack1[-1]:
        stack2.pop()
        stack1.pop()
        moveCounter += 1

if stack1 or stack2:
    sys.stdout.write("impossible")
else:
    sys.stdout.write(str(moveCounter))
