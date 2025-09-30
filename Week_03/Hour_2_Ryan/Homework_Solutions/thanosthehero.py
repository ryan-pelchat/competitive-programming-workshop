"""
Problem Title: Thanos the Hero
Platform: Kattis
Problem URL: https://open.kattis.com/problems/thanosthehero
Difficulty: 2.6 Easy
Categories: 3.2 i. Mathematical Simulation (Complete Search), Harder

Author: Ryan Pelchat
Date Solved: 2025-09-30
Language: Python3

Approach:
    - strategy
        - Need population to be in decrementing order
        - If we can't then print("1")
        - Reverse string and loop forward ensuring the order
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(1)

Notes:
"""

import sys

lines = sys.stdin.read().strip().splitlines()
cases = int(lines[0])
pops = list(map(int, lines[1].split()))[::-1]
deathToll = 0

for i in range(1, len(pops)):
    if pops[i - 1] <= pops[i]:
        diff = (pops[i] - pops[i - 1]) + 1
        deathToll += diff
        pops[i] -= diff
        if pops[i] < 0:
            print(1)
            quit()
print(deathToll)
