"""
Problem Title: grandpabernie
Platform: Kattis
Problem URL: https://open.kattis.com/problems/grandpabernie
Difficulty: 2.5 Easy

Author: Ryan Pelchat
Date Solved: 2025-09-15
Language: Python3

Approach:
    - strategy
        - Read all trips and group years by destination.
        - Sort the list of years for each destination.
        - For each query, retrieve the (k-1)-th element from the sorted
          list of years corresponding to that destination.
    - technique (two pointers, recursion, BFS, etc...)
        - Dictionary (hash map) mapping destinations to lists of years.
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n log n)
Space Complexity: O(n)

Notes:
"""

import sys
from collections import defaultdict

lines = sys.stdin.read().strip().splitlines()

tripNum = int(lines[0])
queryNum = int(lines[tripNum + 1])

output = []

dic = defaultdict(list)

for line in lines[1 : tripNum + 1]:
    tripSplit = line.split()
    destination = tripSplit[0]
    year = int(tripSplit[1])
    dic[destination].append(year)

for key in list(dic.keys()):
    dic[key].sort()

for line in lines[tripNum + 2 :]:
    querySplit = line.split()
    destination = querySplit[0]
    sequenceNum = int(querySplit[1])
    output.append(str(dic[destination][sequenceNum - 1]))

sys.stdout.write("\n".join(output) + "\n")
