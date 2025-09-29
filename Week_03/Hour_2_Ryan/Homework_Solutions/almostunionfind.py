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
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(...)
Space Complexity: O(...)

Notes:
    NOT WORKING YET
"""

import sys
from collections import defaultdict


class Ryan_unionFind:
    """An implementation of the union-find disjoint set data structure


    Attributes:
        _numSet: (int) represents the number of disjoint sets
        _parents: (list[int]) stores the index (points to) of parents
        _ranks: (list[int]) stores the rank of every set
        _sizes: (list[int]) stores the size of every set
        _sums: (list[int]) stores the sum of every set
    """

    def __init__(self, numItems: int) -> None:
        if numItems < 1:
            raise ValueError("numItems needs to be greater or equal to 1")
        numItems += 1
        self._parents = list(range(numItems))
        self._ranks = [0] * numItems
        self._sizes = [1] * numItems
        self._sums = list(range(numItems))

    def __str__(self) -> str:
        self.optimize()
        structure = defaultdict(list)
        output = []
        for idx, element in enumerate(self._parents):
            structure[element].append(idx)

        for key in structure:
            output.append(f"\n{key}\n\t")
            for child in structure[key]:
                output.append(f"{child}, ")
        return "".join(output)

    def __len__(self) -> int:
        return self.getNumDisjointSets()

    def findSet(self, element: int) -> int:
        # to keep track of vertexes travelled to do path compression
        children = []
        toFind = element

        # finding the representative root element
        while toFind != self._parents[toFind]:
            children.append(toFind)
            toFind = self._parents[toFind]

        # path compression
        for c in children:
            self._parents[c] = toFind

        return toFind

    def isSameSet(self, element1: int, element2: int) -> bool:
        return self.findSet(element1) == self.findSet(element2)

    def unionSet(self, element1: int, element2: int) -> None:
        s1 = self.findSet(element1)
        s2 = self.findSet(element2)

        if s1 == s2:
            return None

        # Ensure s2 has greater rank than s1
        if self._ranks[s1] > self._ranks[s2]:
            s1, s2 = s2, s1
        # Increase rank only when equal
        elif self._ranks[s1] == self._ranks[s2]:
            self._ranks[s2] += 1

        # Attach s1 under s2
        self._parents[s1] = s2

        # Update sums
        self._sums[s2] += self._sums[s1]

        # Update sizes
        self._sizes[s2] += self._sizes[s1]

    def sizeOf(self, element) -> int:
        return self._sizes[self.findSet(element)]

    def optimize(self) -> None:
        for i in range(len(self._parents)):
            self.findSet(i)

    def move(self, element1, element2) -> None:
        s1 = self.findSet(element1)
        s2 = self.findSet(element2)

        if s1 == s2:
            return None

        # Move element to new set
        self._parents[element1] = s2

        # Update sums
        self._sums[s1] -= element1
        self._sums[s2] += element1

        self._sizes[s1] -= 1
        self._sizes[s2] += 1

    def getSumOf(self, element) -> int:
        return self._sums[self.findSet(element)]


lines = sys.stdin.read().strip().splitlines()
setSize = int(lines[0].split()[0])

output = []

ufds = Ryan_unionFind(setSize)
for line in lines[1:]:
    values = line.split()
    command = values[0]
    match command:
        case "3":
            p = int(values[1])
            output.append(f"{ufds.sizeOf(p)} {ufds.getSumOf(p)}\n")
        case _:
            p = int(values[1])
            q = int(values[2])
            match command:
                case "1":
                    ufds.unionSet(p, q)
                case "2":
                    ufds.move(p, q)

sys.stdout.write("".join(output))
