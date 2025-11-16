"""
Problem Title: 507 - Jill Rides Again
Platform: UVa
Problem URL: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=448
Difficulty: N/A
Categories: a1. Max 1D Range Sum

Author: Ryan Pelchat
Date Solved: 2025/10/29
Language: Python3

Approach:
    - strategy
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(...)
Space Complexity: O(...)

Notes:
+2 because if there are 3 segments a,b,c then there are 4 stops as follows
    1a2b3c4
    stops a,b,c has indexes 0, 1, 2 respectively
    thus the end stop of a is index 0 + 2 which is 2
"""

import sys
from typing import *

data = iter(sys.stdin.read().strip().split())
output = []
for routeNum in range(int(next(data))):  # going through routes
    candidate = [0, 0, 0]  # [currSum, start, stop]
    maxData = [0, 0, 0]  # [maxSum, start, stop]
    for segmentNum in range(int(next(data)) - 1):
        niceNum = int(next(data))
        candidate[0] += niceNum
        if candidate[0] > maxData[0]:
            candidate[2] = segmentNum + 2  # look at notes for why +2
        if candidate[0] < 0:
            maxData = candidate[::]  # to prevent aliasing
            candidate = [0, segmentNum + 1, segmentNum + 2]
    print(maxData)
