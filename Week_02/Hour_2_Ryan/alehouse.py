"""
Problem Title: Alehouse
Platform: Kattis
Problem URL: https://open.kattis.com/problems/alehouse
Difficulty: 4.1 Medium

Author: Ryan Pelchat
Date Solved: 2025-09-21
Language: Python3

Approach:
    - strategy
        - 2 min Heaps
        - 1 min heap is entry times
        - 1 min heap is exit times
        - For each entry time, push to exitHeap for everyone with
          start ≤ current_time
            - Pop all values in exitHeap that are below our entry time
            - len(exitHeap) is the amount of friends we can make at that
              millisecond
        - return max amount of friends we made
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?
        - make sure you don't pop an empty heapq
        - the timestamps are inclusive (meet at the door case)

Time Complexity: O(n log n)
Space Complexity: O(n)

Notes:
heapq does min heap with first index when it contains tuples

If you read all the input then heapify, it is faster than pushing into
an existing heap

https://docs.python.org/3/library/heapq.html#heapq.heapify

heapify is O(n) while heappush is O(logn)

This code passes Kattis, so I won't change it, but I will leave this note
here.
"""

import sys
import heapq

lines = sys.stdin.read().strip().splitlines()

maxFriends = 0
maxStay = int(lines[0].split()[1])
entryHeap = []
exitHeap = []
targetTime = maxStay

# Sort all the entries
for line in lines[1:]:
    parsedLine = line.split()
    heapq.heappush(entryHeap, (int(parsedLine[0]), int(parsedLine[1])))

# continue algo until no more values remain
while len(entryHeap) > 0:
    # push onto exitHeap during out test time
    while len(entryHeap) > 0 and entryHeap[0][0] <= targetTime:
        heapq.heappush(exitHeap, heapq.heappop(entryHeap)[1])

    while len(exitHeap) > 0 and exitHeap[0] < targetTime - maxStay:
        heapq.heappop(exitHeap)

    if len(exitHeap) > maxFriends:
        maxFriends = len(exitHeap)

    # update to new target time
    if len(entryHeap) > 0:
        targetTime = entryHeap[0][0]

sys.stdout.write(str(maxFriends) + "\n")
