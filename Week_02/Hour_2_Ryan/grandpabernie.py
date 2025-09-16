import sys
from collections import defaultdict

lines = sys.stdin.read().strip().splitlines()

tripNum = int(lines[0])
queryNum = int(lines[tripNum + 1])

output = []

dic = defaultdict(list)

for line in lines[1 : tripNum + 1]:
    tripSplit = line.split()
    destination = tripSplit[0]
    year = int(tripSplit[1])
    dic[destination].append(year)

for key in list(dic.keys()):
    dic[key].sort()

for line in lines[tripNum + 2 :]:
    querySplit = line.split()
    destination = querySplit[0]
    sequenceNum = int(querySplit[1])
    output.append(str(dic[destination][sequenceNum - 1]))

sys.stdout.write("\n".join(output) + "\n")
