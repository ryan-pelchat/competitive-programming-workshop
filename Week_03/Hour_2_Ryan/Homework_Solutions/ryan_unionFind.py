"""ryan_unionFind.py

This is my personal implementation of the union-find disjoint set

"""


class ryan_unionFind:
    """An implementation of the union-find disjoint set data structure


    Attributes:
        _numDisjointSets: (int) represents the number of disjoint sets
        _elements: (list[int]) stores all the values
        _ranks: (list[int]) stores the rank of every set
        _sizeOfSets: (list[int]) stores the size of every set
    """

    def __init__(self, numItems: int, numSets: int = None) -> None:
        """Initializes the data structure

        Args:
            numItems: (int) number of elements to create
            numSets: (int) number of starting sets to create
                        (default is that numItems == numSets)
        """
        if numSets is None:
            numSets = numItems
        else:
            pass
        self._numDisjointSets = numItems
        self._elements = list(range(numItems))
        self._ranks = [0] * numItems
        self._sizeOfSets = [1] * numItems

    def findSet(self, element: int) -> int:
        """Finds the representative item of a set
            (finds which set element belongs to)

        As it recursively finds the answer, it does path compression
        which optimizes the search for the root element

        Args:
            element (int): The file location of the spreadsheet

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
        while toFind != self._elements[element]:
            children.append(element)
            toFind = self._elements[element]

        # path compression
        for element in children:
            self._elements[element] = toFind

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

        if self._ranks[s1] > self._ranks[s2]:
            s1, s2 = s2, s1
        self._elements[s1] = s2
        self._ranks[s2] += 1

        self._numDisjointSets -= 1
        self._sizeOfSets[s2] += self._sizeOfSets[s1]

    def getNumDisjointSets(self) -> int:
        """Returns the number of disjoint sets currently stored

        Returns:
            int: the number of disjoint sets currently stored
        """
        return self._numDisjointSets

    def sizeOf(self, element) -> int:
        """Returns the size of the set that element is a part of

        Args:
            element (int): element that is part of a set that we want to
                            find the size of

        Returns:
            int: The size of the set that element is a part of
        """
        return self._sizeOfSets[element]
