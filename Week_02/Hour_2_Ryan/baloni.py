"""
Problem Title: baloni
Platform: Kattis
Problem URL: https://open.kattis.com/problems/baloni
Difficulty: 2.0 Medium

Author: Ryan Pelchat
Date Solved: 2025-09-15
Language: Python3

Approach:
    - strategy
        - Keep track of arrows currently in flight at each height.
        - When a balloon at height h is encountered:
            - If there is an arrow at height h+1, that arrow will pop
              this balloon and continue at height h (so decrement h+1
              and increment h).
            - Otherwise, start a new arrow at height h.
        - At the end, the sum of arrows in the array is the answer.
    - technique (two pointers, recursion, BFS, etc...)
        - Array used as a hash map keyed by height
    - why did you choose it?
        - Using an array indexed by height avoids the overhead of a true
          hash map and ensures O(1) updates per balloon.
    - edge cases considered?

Time Complexity: O(n)
    - Each balloon leads to at most two constant-time operations.
Space Complexity: O(H)
    - Where H is the maximum balloon height (array of size up to 1e6+2).

Notes:
- This array-based "hash map" approach is much faster than the naive
  nested loop (O(n^2)).
"""

import sys
from typing import *


import sys

# sys.getsizeof() returns size in bytes

lines = sys.stdin.read().strip().splitlines()
heights = list(map(int, lines[1].split()))

subsequences = []
# range does not include last number, and I need one beyond to account
# for the max digit edge case
subsequences = [0 for i in range(1000002)]

for height in heights:
    # check if a baloon is 1 higher than it
    if subsequences[height + 1] == 0:
        # if not then start arrow at this height
        subsequences[height] += 1
    else:
        # if there is, then an arrow is going to hit it
        # move the arrow height to new height
        subsequences[height + 1] -= 1
        subsequences[height] += 1
print(sum(subsequences))

# n^2 in worse case below
# in worse case, similar to double for loop solution
# # initialize subsequences
# subsequences.append([heights[0]])

# for height in heights[1:]:
#     added = False
#     for i in range(len(subsequences)):
#         if height == subsequences[i][-1] - 1:
#             subsequences[i].append(height)
#             added = True
#             break
#     if not added:
#         subsequences.append([height])
# print(len(subsequences))
