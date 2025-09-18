from typing import *
import sys

lines = sys.stdin.read().strip().splitlines()
direction = int(lines.pop())
mainGrid = [list(map(int, row.split())) for row in lines]
# print(mainGrid)
output = []


def rotate90Clockwise(mat: list[list[int]]):
    # reverses, unpacks, zips
    return [list(row) for row in zip(*mat[::-1])]


def smashTogetherLeft(grid: list[list[int]]):
    newGrid = []
    for row in grid:
        newRow = []
        combinedToggle = False
        for value in row:
            # if newRow is empty

            if not newRow and value != 0:
                newRow.append(value)
            elif newRow:
                if newRow[-1] == value and not combinedToggle:
                    newRow[-1] += value
                    combinedToggle = True
                elif value != 0:
                    newRow.append(value)
                    combinedToggle = False
        while len(newRow) < 4:
            newRow.append(0)
        newGrid.append(newRow)
    return newGrid


match direction:
    case 0:
        mainGrid = smashTogetherLeft(mainGrid)
        sys.stdout.write("\n".join([" ".join(list(map(str, row))) for row in mainGrid]))
    case 1:
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = smashTogetherLeft(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        sys.stdout.write("\n".join([" ".join(list(map(str, row))) for row in mainGrid]))
    case 2:
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = smashTogetherLeft(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        sys.stdout.write("\n".join([" ".join(list(map(str, row))) for row in mainGrid]))

    case 3:
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = smashTogetherLeft(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        mainGrid = rotate90Clockwise(mainGrid)
        sys.stdout.write("\n".join([" ".join(list(map(str, row))) for row in mainGrid]))
