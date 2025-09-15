import sys

lines = sys.stdin.read().strip().splitlines()
output = []
tempSequence = []
previousNumber = float("-inf")

for number in lines[1].split():
    if int(number) > previousNumber:
        tempSequence.append(number)
        previousNumber = int(number)

output.append(str(len(tempSequence)))
output.append(" ".join(tempSequence))
output.append("\n")
sys.stdout.write("\n".join(output))
