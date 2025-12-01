"""
Problem Title: snapperhard
Platform: Kattis
Problem URL: https://open.kattis.com/problems/snapperhard
Difficulty: 2.2 Easy

Author: Ryan Pelchat
Date Solved: 2025-11-25
Language: Python3

Approach:
    - strategy
        - Draw out an example case:
            - below, on lights are 1, off lights are 0, power comes from the right
            - assume there are 3 lights, between states there is a clap
            - state 0: 000
            - state 1: 001
            - state 2: 010
            - state 3: 011
            - state 4: 100
            - One can observe that it is counting in binary
        - Thus the problem can be rephrased as follows:
            - When K is represented in bits, are all lower N bits 1s?
                - i.e. for K claps, are all N snappers turned on?
        - Apply an N bit mask of 1s to K bit string
        - If all lower N bits are 1s then ON, otherwise OFF
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
- The unknown values mirror the short-circuit evaluation style of logic
    in Python.
"""

import sys

data = sys.stdin.read().strip().splitlines()

for idx, case in enumerate(data[1:]):
    n, k = list(map(int, case.split()))
    mask = (1 << n) - 1  # check if all lower bits below n are turned on
    if (k & mask) == mask:  # all n low bits are 1
        print(f"Case #{idx+1}: ON")
    else:
        print(f"Case #{idx+1}: OFF")
