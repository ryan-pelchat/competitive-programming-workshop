"""
Problem Title: bitbybit
Platform: Kattis
Problem URL: https://open.kattis.com/problems/bitbybit
Difficulty: 2.7 Easy

Author: Ryan Pelchat
Date Solved: 2025-11-25
Language: Python3

Approach:
    - strategy
        - Implement set and clear bit, they are trivial.
        - Create a new truth table for orBit and andBit taking into account
            how unknown values affect the end result. See function comments.
    - technique (two pointers, recursion, BFS, etc...)
    - why did you choose it?
    - edge cases considered?
        - some operations with unknown values result in known values

Time Complexity: O(n)
Space Complexity: O(n)

Notes:
- The unknown values mirror the short-circuit evaluation style of logic
    in Python.
"""

import sys


def clear(i: int, binary: int, output: list[str]) -> int:
    """
    Puts a zero into bit i

    Returns the new binary and modifies the output to match the binary
    representation
    """
    binary &= ~(1 << i)
    output[i] = "0"
    return binary


def setBit(i: int, binary: int, output: list[str]) -> int:
    """
    Put a one into bit i

    Returns the new binary and modifies the output to match the binary
    representation
    """
    binary |= 1 << i
    output[i] = "1"
    return binary


def orBit(i: int, j: int, binary: int, output: list[str]) -> int:
    """
    Store in bit i the logical OR of the contents of bits i and j.

    Returns the new binary and modifies the output to match the binary
    representation

    T, F, G, ? are 1, 0, regular truth table evaluation, ? respectively

    OR |value stored
    ? ?|?
    ? 1|1
    ? 0|?
    G G|G
    0 ?|?
    1 ?|1
    """
    if output[i] != "?" and output[j] != "?":
        # proceed as usual, case G G
        if not (binary & (1 << i)) and (not (binary & (1 << j))):
            return clear(i, binary, output)
        else:
            return setBit(i, binary, output)
    elif output[i] == "1" or output[j] == "1":
        # check if either i or j are 1s
        return setBit(i, binary, output)
    else:
        # if at this point i or j are anyting but 1s then ?
        output[i] = "?"
        return binary


def andBit(i: int, j: int, binary: int, output: list[str]) -> int:
    """
    Store in bit i the logical AND of the contents of bits i and j.

    Returns the new binary and modifies the output to match the binary
    representation

    T, F, G, ? are 1, 0, regular truth table evaluation, ? respectively

    AND|value stored
    ? ?|?
    ? 1|?
    ? 0|0
    G G|G
    0 ?|0
    1 ?|?
    """
    if output[i] != "?" and output[j] != "?":
        # proceed as usual, case G G
        if (binary & (1 << i)) and (binary & (1 << j)):
            return setBit(i, binary, output)
        else:
            return clear(i, binary, output)
    elif output[i] == "0" or output[j] == "0":
        # check if either i or j are 0s
        return clear(i, binary, output)
    else:
        # if at this point i or j are anyting but 0s then ?
        output[i] = "?"
        return binary


data = iter(sys.stdin.read().strip().splitlines())

output = ["?" for _ in range(32)]
binary = 0

counter = int(next(data))

while counter > 0:
    counter -= 1
    command = next(data).split()
    match command[0]:
        case "SET":
            binary = setBit(int(command[1]), binary, output)
        case "CLEAR":
            binary = clear(int(command[1]), binary, output)
        case "AND":
            i = int(command[1])
            j = int(command[2])
            binary = andBit(i, j, binary, output)
        case "OR":
            i = int(command[1])
            j = int(command[2])
            binary = orBit(i, j, binary, output)
    if counter <= 0:
        counter = int(next(data))
        sys.stdout.write("".join(output[::-1]) + "\n")
        output = ["?" for _ in range(32)]

# sys.stdout.write("".join(output[::-1]))
