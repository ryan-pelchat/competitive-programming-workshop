"""
Problem Title: bracketmatching
Platform: Kattis
Problem URL: https://open.kattis.com/problems/bracketmatching
Difficulty: 2.1 Easy
Categories:

Author: Ryan Pelchat
Date Solved: 2025-09-15
Language: Python3

Approach:
    - strategy
        - loop over bracket symbols
            - stack open brackets
            - if close bracket and it matches with top of open bracket
              stack, then pop open bracket
                - if doesn't match or open bracket stack is empty then
                  print Invalid
        - if at the end the stack is empty, then print Valid
    - technique (two pointers, recursion, BFS, etc...)
        - stack
    - why did you choose it?
    - edge cases considered?

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
"""

from typing import *
import sys

lengthOfBracketSqn = int(input())
bracketSqn = input()


def parenthesesMatching(string: str) -> bool:
    stack = []
    bracketMatching = {"(": ")", "{": "}", "[": "]"}

    for s in string:
        if s in bracketMatching.keys():  # opening
            stack.append(s)
        elif s in bracketMatching.values():  # closing
            if not stack or bracketMatching[stack[-1]] != s:
                return False
            stack.pop()

    return not stack


if parenthesesMatching(bracketSqn):
    print("Valid")
else:
    print("Invalid")
