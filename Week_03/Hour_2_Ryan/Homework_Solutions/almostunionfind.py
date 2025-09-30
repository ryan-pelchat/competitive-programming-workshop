"""
Problem Title: Almost Union-Find
Platform: Kattis
Problem URL: https://open.kattis.com/problems/almostunionfind?tab=metadata
Difficulty: 4.0 Medium
Categories: 2.4 b. Union-Find Disjoint Sets

Author: Ryan Pelchat
Date Solved: 2025-09-29
Language: Python3

Approach:
    - strategy
        - Model each set using a disjoint-set union (union-find) structure.
        - Maintain an array idx[x] mapping each original element x to its
          current DSU node. On a move operation, mint a new node for x,
          reattach it under the target set's root, and update idx[x].
        - Track both the size and sum of each set in arrays indexed by
          representative nodes.
    - technique (two pointers, recursion, BFS, etc...)
        - Union-Find Disjoint Set (DSU) with path compression.
        - Augmented with per-set metadata (size and sum)
        - idx array to keep track of mapping which nodes point to which
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(1)
    - effectively constant (amortized O(a(n+m)) per operation (inverse Ackermann))
Space Complexity: O(n + m)

Notes:
    - At any time, idx[x] tells you which DSU node ID currently stands for
      element x.
    - If you move x, you mint a fresh node and update idx[x] to point to the
      new node.
    - Only root nodes store meaningful size/sum aggregates; non-root values
      are not used in queries.
"""

import sys
from collections import defaultdict


class Ryan_unionFind:
    """An implementation of the union-find disjoint set data structure"""

    def __init__(self, numItems: int) -> None:
        if numItems < 1:
            raise ValueError("numItems needs to be greater or equal to 1")
        numItems += 1
        self._parents = list(range(numItems + 1))
        self._sizes = [1] * (numItems + 1)
        self._idx = list(range(numItems + 1))
        self._sums = list(range(numItems + 1))

    def findSet(self, element: int) -> int:
        while element != self._parents[element]:
            # path compression as you traverse
            self._parents[element] = self._parents[self._parents[element]]
            element = self._parents[element]
        return element

    def isSameSet(self, element1: int, element2: int) -> bool:
        return self.findSet(self._idx[element1]) == self.findSet(self._idx[element2])

    def unionSet(self, element1: int, element2: int) -> None:
        s1 = self.findSet(self._idx[element1])
        s2 = self.findSet(self._idx[element2])

        if s1 == s2:
            return None

        if self._sizes[s1] > self._sizes[s2]:
            s1, s2 = s2, s1

        self._parents[s1] = s2

        self._sizes[s2] += self._sizes[s1]

        self._sums[s2] += self._sums[s1]

    def move(self, element1: int, element2: int) -> None:
        # Move element1 into the set that currently contains element2
        s1 = self.findSet(self._idx[element1])
        s2 = self.findSet(self._idx[element2])

        if s1 == s2:
            return None

        # update sizes and sums for s1
        self._sizes[s1] -= 1
        self._sums[s1] -= element1

        # Create a new node for element1
        self._parents.append(s2)
        self._sizes.append(1)
        self._sums.append(element1)

        # update sizes and sums for s2
        self._sizes[s2] += 1
        self._sums[s2] += element1

        # Update mapping so element1 now refers to the fresh node
        self._idx[element1] = len(self._parents) - 1

    def getSumOf(self, element) -> int:
        return self._sums[self.findSet(self._idx[element])]

    def getSizeOf(self, element: int) -> int:
        return self._sizes[self.findSet(self._idx[element])]


lines = sys.stdin.read().strip().splitlines()
output = []
i = 0
while i < len(lines):
    n, m = map(int, lines[i].split())
    ufds = Ryan_unionFind(n)
    for _ in range(m):
        i += 1
        values = list(map(int, lines[i].split()))
        match values[0]:
            case 1:
                ufds.unionSet(values[1], values[2])
            case 2:
                ufds.move(values[1], values[2])
            case 3:
                output.append(
                    f"{ufds.getSizeOf(values[1])} {ufds.getSumOf(values[1])}\n"
                )
    i += 1

sys.stdout.write("".join(output))
