"""basicFenwickTemplate.py
This is my own implementation of the basic features for a Fenwick Tree

"""

from collections import defaultdict


class FTree:
    """An implementation of a basic Fenwick Tree

    Attributes:
        _n: (int) represents the length of the original input values
        _ft: (list[int]) stores the fenwick tree
    """

    def __init__(self, f):
        """
        Creates a new instance of the basic Fenwick Tree.

        Arguments:
            f: (list[int]) data to build your Fenwick Tree

        Example:

        """
        self._n = len(f)
        self._ft = [0] * (self._n + 1)

        for i in range(1, self._n + 1):
            self._ft[i] += f[i - 1]
            if i + self.lsone(i) <= self._n:
                self._ft[i + self.lsone(i)] += self._ft[i]

    def lsone(self, i):
        return i & -i

    def rsq(self, i):
        sum = 0
        while i > 0:
            sum += self._ft[i]
            i -= self.lsone(i)
        return sum

    def rsq2(self, i, j):
        if i > 1:
            return self.rsq2(1, j) - self.rsq2(1, i - 1)
        return self.rsq(j)

    def update(self, i, v):
        while i <= self._n:
            self._ft[i] += v
            i += self.lsone(i)
