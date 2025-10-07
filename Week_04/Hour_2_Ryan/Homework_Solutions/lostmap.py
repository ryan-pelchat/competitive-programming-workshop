"""
Problem Title: Lost Map
Platform: Kattis
Problem URL: https://open.kattis.com/problems/lostmap
Difficulty: 1.9 Easy
Categories: 4.3 Minimum Spanning Tree (MST) a. Standard

Author: Ryan Pelchat
Date Solved: 2025-10-07
Language: Python3

Approach:
    - strategy
        - Given a fully connected graph (each village connected to every other),
          where each edge weight represents the cost of building a road,
          we must determine which roads (edges) form the Minimum Spanning Tree.
        - This ensures all villages are connected with minimal total cost.
    - technique (two pointers, recursion, BFS, etc...)
        - Kruskal's Algorithm
            1. Convert the input adjacency matrix into an edge list of tuples:
               (weight, vertex1, vertex2).
            2. Sort the edges by ascending weight.
            3. Iterate through edges, adding each one that connects two
               previously unconnected components, using a Union-Find (Disjoint Set)
               to efficiently track connected components.
            4. Stop once n - 1 edges are added.
        - Union-Find with path compression and union by rank is used
          to optimize disjoint set operations.
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(E log V)
    - Kruskal
Space Complexity: O(E + V)

Notes:
"""

import sys
from typing import *

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
        ru = ufds.findSet(u)
        rv = ufds.findSet(v)
        if ru != rv:
            ufds.unionSet(ru, rv)
            edgeListOutput.append((w, u, v))
            totalMSTweight += w
    return (edgeListOutput, totalMSTweight)


lines = sys.stdin.read().strip().splitlines()
grid = [list(map(int, line.split())) for line in lines[1:]]
numVertex = int(lines[0])
output = []
edgeList = []
for row in range(numVertex):
    for col in range(row, numVertex):
        edgeList.append((grid[row][col], row, col))
for edge in ryan_kruskal(numVertex, edgeList)[0]:
    output.append(f"{edge[1]+1} {edge[2]+1}\n")
sys.stdout.write("".join(output))
