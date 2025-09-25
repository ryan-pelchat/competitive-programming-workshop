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
        self._numDisjointSets = numItems
        self._elements = [i for i in range(numItems)]
        self._ranks = [0 for _ in range(numItems)]
        self._sizeOfSets = [1 for _ in range(numItems)]

    def findSet(self, element: int) -> int:
        """Finds the representative item of a set
            (finds which set element belongs to)

        Args:
            element (int): The file location of the spreadsheet

        Returns:
            int: the root of the set that element belongs to
        """
        pass

    # def initialize(numItems: int, numSets: int):
    #     """Gets and prints the spreadsheet's header columns

    #     Args:
    #         file_loc (str): The file location of the spreadsheet
    #         print_cols (bool): A flag used to print the columns to the console
    #             (default is False)

    #     Returns:
    #         list: a list of strings representing the header columns
    #     """
