"""
Problem Title:
Platform:
Problem URL:
Difficulty:
Categories:

Author: Ryan Pelchat
Date Solved:
Language: Python3

Approach:
    - strategy
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(...)
Space Complexity: O(...)

Notes:
"""

import sys
from typing import *

"""UnionFind.py

This is my personal implementation of the union-find disjoint set

"""

"""UnionFind.py

This is my personal implementation of the union-find disjoint set

"""

from collections import defaultdict
import random


class UnionFind:
    """An implementation of the union-find disjoint set data structure


    Attributes:
        _numSet: (int) represents the number of disjoint sets
        _parents: (list[int]) stores the index (points to) of parents
        _ranks: (list[int]) stores the rank of every set
        _sizes: (list[int]) stores the size of every set
    """

    def __init__(self, numItems: int, numSets: int = None) -> None:
        """Initializes the data structure

        Args:
            numItems: (int) number of elements to create
                        (must be greater than 1)
            numSets: (int) number of starting sets to create
                        (default is that numItems == numSets)
                        (must be greater or equal to 1 and smaller than
                        numItems)

        Raises:
            ValueError:
                numItems < 1
                numItems < numSets
        """
        if numItems < 1:
            raise ValueError("numItems needs to be greater or equal to 1")
        elif numSets is not None and numItems < numSets:
            raise ValueError("numSets must not be greater than numItems")

        self._numSet = numItems
        self._parents = list(range(numItems))
        self._ranks = [0] * numItems
        self._sizes = [1] * numItems
        if numSets is None:
            numSets = numItems
        else:
            while self._numSet > numSets:
                self.unionSet(random.randrange(numItems), random.randrange(numItems))

    def __str__(self) -> str:
        """Returns a string representation of this object

        Note:
            Runtime is slower

        Returns:
            str: string representation of this object
        """
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
        """Returns the number of disjoint sets currently stored

        Returns:
            int: the number of disjoint sets currently stored
        """
        return self.getNumDisjointSets()

    def findSet(self, element: int) -> int:
        """Finds the representative item of a set
            (finds which set element belongs to)

        As it iteratively finds the answer, it does path compression
        which optimizes the search for the root element

        Args:
            element (int): The element fo find the set it is part of

        Notes:
            I initially implemented this recursively, but in the edge case
            for a very tall graph, it could extend pass the maximum stack
            height

        Returns:
            int: the root of the set that element belongs to
        """
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
        """Finds out if element1 and element2 are part of the same set

        Args:
            element1 (int): The first element to check
            element2 (int): The second element to check

        Returns:
            bool: True if they are part of the same set, False otherwise
        """
        return self.findSet(element1) == self.findSet(element2)

    def unionSet(self, element1: int, element2: int) -> None:
        """Unite a disjoint set that contains element1 with a different
            disjoint set that contains element2

        Args:
            element1 (int): The first element
            element2 (int): The second element
        """
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

        self._numSet -= 1
        self._sizes[s2] += self._sizes[s1]

    def getNumDisjointSets(self) -> int:
        """Returns the number of disjoint sets currently stored

        Returns:
            int: the number of disjoint sets currently stored
        """
        return self._numSet

    def sizeOf(self, element) -> int:
        """Returns the size of the set that element is a part of

        Args:
            element (int): element that is part of a set that we want to
                            find the size of

        Returns:
            int: The size of the set that element is a part of
        """
        return self._sizes[self.findSet(element)]

    def optimize(self) -> None:
        """Runs the path compression on every element in data structure"""
        for i in range(len(self._parents)):
            self.findSet(i)


# processing input
lines = sys.stdin.read().strip().splitlines()
n = int(lines[0].split()[0])
output = []

ufds = UnionFind(n)

# going through every command
for command in lines[1:]:
    line = command.split()
    op = line[0]
    e1 = int(line[1])
    e2 = int(line[2])

    match op:
        case "?":
            output.append("yes\n" if ufds.isSameSet(e1, e2) else "no\n")
        case "=":
            ufds.unionSet(e1, e2)

sys.stdout.write("".join(output))
