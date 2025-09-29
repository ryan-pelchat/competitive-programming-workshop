"""
Problem Title: Geppetto
Platform: Kattis
Problem URL: https://open.kattis.com/problems/geppetto
Difficulty: 2.2 Easy
Categories: 3.2 f. Iterative (Combination)

Author: Ryan Pelchat
Date Solved:
Language: Python3

Approach:
    - strategy
        - Represent each pizza topping choice as a bit in a bitmask
        - Enumerate all subsets of toppings using bit tricks.
        - For each subset, check if it contains any illegal pair of toppings.
        - If no illegal pair is present, count it as a valid pizza.
    - technique (two pointers, recursion, BFS, etc...)
        - Bitmask subset enumeration.
        - Bitwise checks for illegal pairs.
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(2^N * M)
    - 2^N subsets to check, each requires scanning up to M illegal pairs.
Space Complexity: O(M)

Notes:
     - Bitmask enumeration (subset - 1) & mask generates all subsets
       efficiently in decreasing order.
"""

import sys
import itertools

lines = sys.stdin.read().strip().splitlines()
N = int(lines[0].split()[0])
mask = (1 << N) - 1

illegalPairs = []
for line in lines[1:]:
    a, b = map(int, line.split())
    illegalPairs.append((a - 1, b - 1))

count = 0
subset = mask
while True:
    # valid if no illegal pair (a,b) is fully contained in subset
    valid = True
    for a, b in illegalPairs:
        if (subset & (1 << a)) and (subset & (1 << b)):
            valid = False
            break
    if valid:
        count += 1

    if subset == 0:
        break
    subset = (subset - 1) & mask  # next subset
print(count)
