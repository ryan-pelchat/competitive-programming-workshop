"""
Problem Title: Svemir
Platform: Kattis
Problem URL: https://open.kattis.com/problems/svemir
Difficulty: 5.1 Medium
Categories: 4.3 Minimum Spanning Tree (MST) a. Standard

Author: Ryan Pelchat
Date Solved:
Language: Python3

Approach:
    - Strategy
        - Attach the original index to each planet: (id, x, y, z).
        - Sort the planets separately by x, by y, and by z.
        - For each sorted list, add an edge only between consecutive pairs;
        set the edge weight to min(|Δx|, |Δy|, |Δz|).
        - Run Kruskal's algorithm on this ~3(n-1) edge set to get the MST cost.
        - Why this works
            - For any cut, a minimum-cost edge crossing the cut attains its cost on one axis.
            On that axis' sorted order, its endpoints must be consecutive across the cut;
            otherwise there exists a strictly cheaper crossing edge. By the cut property,
            keeping only consecutive neighbors per axis is sufficient.
    - technique (two pointers, recursion, BFS, etc...)
        - Sorting (3 axis sorts)
        - Union-Find (path compression + union by rank)
        - Kruskal's algorithm
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n log n)  (three O(n log n) sorts + Kruskal over ~3n edges)
Space Complexity: O(n)       (points, edges, DSU)

Notes:
"""

"""ryan_mst.py
This MST implementation is implemented using Kruskal
"""

"""ryan_unionFind.py

This is my personal implementation of the union-find disjoint set

"""


class Ryan_unionFind:
    """An implementation of the union-find disjoint set data structure


    Attributes:
        _numSet: (int) represents the number of disjoint sets
        _parents: (list[int]) stores the index (points to) of parents
        _ranks: (list[int]) stores the rank of every set
        _sizes: (list[int]) stores the size of every set
    """

    def __init__(self, numItems: int) -> None:
        """Initializes the data structure

        Args:
            numItems: (int) number of elements to create
                        (must be greater than 1)

        Raises:
            ValueError:
                numItems < 1
                numItems < numSets
        """
        if numItems < 1:
            raise ValueError("numItems needs to be greater or equal to 1")

        self._numSet = numItems
        self._parents = list(range(numItems))
        self._ranks = [0] * numItems
        self._sizes = [1] * numItems

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

    def unionSet(self, element1: int, element2: int) -> bool:
        """Unite a disjoint set that contains element1 with a different
            disjoint set that contains element2

        Args:
            element1 (int): The first element
            element2 (int): The second element

        Returns:
            bool: True if merged, False if elements in same set
        """
        s1 = self.findSet(element1)
        s2 = self.findSet(element2)

        if s1 == s2:
            return False

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

        return True

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


def ryan_kruskal(
    numVertex: int, edgeList: list[tuple[int, int, int]]
) -> tuple[list[tuple[int, int, int]], int]:
    """
    This function calculates the MST of a graph represented by the edgeList
    and numVertex.

    Args:
        numVertex (int): number of vertices in the graph
        edgeList (list[tuple[int, int, int]]): an edge list for the graph where
            the tuple is [weight, vertex1, vertex2]

    Returns:
        tuple[list[tuple[int, int, int]]]: an edge list of the MST of the original graph
            and the total weight of the MST
    """
    edges = sorted(edgeList, key=lambda x: -x[0])
    ufds = Ryan_unionFind(numVertex)
    edgeListOutput = []
    totalMSTweight = 0
    while edges and len(edgeListOutput) < numVertex - 1:
        w, u, v = edges.pop()
        if ufds.unionSet(u, v):
            edgeListOutput.append((w, u, v))
            totalMSTweight += w
    return (edgeListOutput, totalMSTweight)


import sys
from typing import *


def tunnelCost(coor1, coor2) -> int:
    return min(
        abs(coor1[0] - coor2[0]), abs(coor1[1] - coor2[1]), abs(coor1[2] - coor2[2])
    )


lines = sys.stdin.read().strip().splitlines()
numPlanets = int(lines[0])
coords = []
for idx, line in enumerate(lines[1:]):
    x, y, z = map(int, line.split())
    coords.append([x, y, z, idx])
# coords = [list(map(int, coord.split())) for idx, coord in enumerate(lines[1:])]

edgeList = []
xsorted = sorted(coords, key=lambda x: x[0])
ysorted = sorted(coords, key=lambda x: x[1])
zsorted = sorted(coords, key=lambda x: x[2])
for i in range(len(coords) - 1):
    edgeList.append(
        (
            tunnelCost(xsorted[i], xsorted[i + 1]),
            xsorted[i][3],
            xsorted[i + 1][3],
        )
    )
    edgeList.append(
        (
            tunnelCost(ysorted[i], ysorted[i + 1]),
            ysorted[i][3],
            ysorted[i + 1][3],
        )
    )
    edgeList.append(
        (
            tunnelCost(zsorted[i], zsorted[i + 1]),
            zsorted[i][3],
            zsorted[i + 1][3],
        )
    )

print(ryan_kruskal(numPlanets, edgeList)[1])
