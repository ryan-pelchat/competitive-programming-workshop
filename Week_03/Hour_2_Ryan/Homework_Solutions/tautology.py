"""
Problem Title: Tautology
Platform: Kattis
Problem URL: https://open.kattis.com/problems/tautology
Difficulty: 2.5 Easy
Categories: 3.2 d. Iterative (Three or More Nested Loops, Harder)

Author: Ryan Pelchat
Date Solved: 2025-09-29
Language: Python3

Approach:
    - strategy
        - Evaluate the formula (given in Polish notation) under all truth
          assignments of its variables and check whether it is always True.
        - Parse recursively from left to right. Each call returns the value of
          the subexpression and the next index to continue parsing.
        - For each test case, enumerate all assignments of the variables that
          actually appear in the formula (subset of {p,q,r,s,t}).
    - technique (two pointers, recursion, BFS, etc...)
        - Recursive descent parser for prefix (Polish) logic.
        - Simple boolean evaluator with operators:
            N (NOT), K (AND), A (OR), C (implication), E (equivalence).
        - Bitmask enumeration of assignments.
    - why did you choose it?
        - With at most 5 variables, brute-forcing all 2^k assignments is okay
    - edge cases considered?
        - Unary NOT chains (e.g., N N p)
        - Early exit on first falsifying assignment

Time Complexity: O(2^k * n)
    - O(2^k * n), where k ≤ 5 is the number of distinct variables in the
        formula and n is the formula length. Worst case is 32 * n.
Space Complexity: O(h)
    - O(h) recursion stack

Notes:
    - The parser always returns (value, next_index); next_index is used to
      chain parses for binary operators
    - Variable order for bitmasks is stable via a sorted list of variables
"""

import sys

lines = sys.stdin.read().strip().splitlines()
output = []
values = {}


def basicEval(command, pt1, pt2=None) -> bool:
    match command:
        case "K":
            return pt1 and pt2
        case "A":
            return pt1 or pt2
        case "N":
            return not pt1
        case "C":
            return (not pt1) or pt2
        case "E":
            return pt1 == pt2


def evaluate(formula, variables, index=0) -> tuple[bool, int]:
    """returns a tuple of value and end of index"""
    c = formula[index]
    if c in "pqrst":
        return variables[c], index + 1
    if c == "N":
        value1, index1 = evaluate(formula, variables, index + 1)
        return basicEval("N", value1), index1

    # binary operator: parse left then right
    v1, i1 = evaluate(formula, variables, index + 1)
    v2, i2 = evaluate(formula, variables, i1)
    return basicEval(c, v1, v2), i2


for line in lines:
    if line == "0":
        break

    # collect and stabilize variable order
    variablesToUse = sorted({ch for ch in line if ch in "pqrst"})
    k = len(variablesToUse)

    tautology = True
    for mask in range(1 << k):  # include all-zero assignment
        for idx, variable in enumerate(variablesToUse):
            values[variable] = bool(mask & (1 << idx))
        val, _ = evaluate(line, values, 0)
        if not val:
            tautology = False
            break

    output.append("tautology\n" if tautology else "not\n")

sys.stdout.write("".join(output))
