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
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(...)
Space Complexity: O(...)

Notes:
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


def evaluate(formula, variables, index=0, level: int = 0) -> bool:
    if formula[index] in "pqrst":
        return variables[formula[index]]
    elif formula[index] == "N" and formula[index + 1] in "pqrst":
        return basicEval(formula[index], variables[formula[index + 1]])
    elif formula[index + 1] in "pqrst" and formula[index + 2] in "pqrst":
        return basicEval(
            formula[index], variables[formula[index + 1]], variables[formula[index + 2]]
        )
    else:
        return basicEval(
            formula[index],
            evaluate(formula, variables, index + 1),
            evaluate(formula, variables, index + 2),
        )


for line in lines[:-1]:
    # find the possible variables
    variablesToUse = set()
    for char in line:
        if char in ["p", "q", "r", "s", "t"]:
            variablesToUse.add(char)

    count = (1 << len(variablesToUse)) - 1
    variablesToUse = list(variablesToUse)
    tautology = True
    while count:
        for idx, variable in enumerate(variablesToUse):
            values[variable] = bool(count & (1 << idx))
        if not evaluate(line, values):
            tautology = False
            break
        count -= 1
    if not tautology:
        output.append("not\n")
    else:
        output.append("tautology\n")

sys.stdout.write("".join(output))
