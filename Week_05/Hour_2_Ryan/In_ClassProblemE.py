import sys
from collections import defaultdict

lines = sys.stdin.read().strip().splitlines()

output = []
cntSet = set()

values = int(lines[0])
draws = [line.split() for line in lines[1:]]

counting = defaultdict(int)

for draw in draws:
    for value in draw:
        counting[value] += 1
        if counting[value] > 2 * values:
            cntSet.add(value)


output = [str(x) for x in sorted([int(val) for val in cntSet])]

if output:
    sys.stdout.write(" ".join(output))
else:
    sys.stdout.write("-1")
