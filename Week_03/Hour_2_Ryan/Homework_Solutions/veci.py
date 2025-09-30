"""
Problem Title: Veci
Platform: Kattis
Problem URL: https://open.kattis.com/problems/veci
Difficulty: 1.5 Easy
Categories: 3.2 e. Iterative (Permutation)

Author: Ryan Pelchat
Date Solved:
Language: Python3

Approach:
    - strategy
        - Generate all permutations of the number
        - Loop and push to a min heap all permutations that are larger
          than number
        - Pop top and return
    - technique (two pointers, recursion, BFS, etc...)
        - Min heap
        - permutations
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n · n! + n! · log(n!)) = O(n · n! · log n)
    - Generating n! permutations and converting each to int/string costs O(n · n!).
    - Each qualifying candidate push to the heap can be O(log n!) = O(n log n) in the worst case,
      yielding O(n! · n log n) overall.

Space Complexity: O(n · n!)
    - Materializing all permutations as a list of tuples is O(n · n!).
    - The candidate min-heap can hold up to O(n!) integers.

Notes:
"""

import sys
import itertools
import heapq

lines = sys.stdin.read().strip().splitlines()
ogNumber = int(lines[0])
numbers = [x for x in lines[0]]
candidateNumbers = []
permutations = [
    int("".join(x)) for x in list(itertools.permutations(numbers, len(numbers)))
]

for permu in permutations:
    if permu > ogNumber:
        heapq.heappush(candidateNumbers, permu)

if not candidateNumbers:
    print(0)
else:
    print(heapq.heappop(candidateNumbers))
