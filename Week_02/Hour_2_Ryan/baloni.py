import sys

# sys.getsizeof() returns size in bytes

lines = sys.stdin.read().strip().splitlines()
heights = list(map(int, lines[1].split()))

subsequences = []
# range does not include last number, and I need one beyond to account
# for the max digit edge case
subsequences = [0 for i in range(1000002)]

for height in heights:
    # check if a baloon is 1 higher than it
    if subsequences[height + 1] == 0:
        # if not then start arrow at this height
        subsequences[height] += 1
    else:
        # if there is, then an arrow is going to hit it
        # move the arrow height to new height
        subsequences[height + 1] -= 1
        subsequences[height] += 1
print(sum(subsequences))

# n^2 in worse case below
# in worse case, similar to double for loop solution
# # initialize subsequences
# subsequences.append([heights[0]])

# for height in heights[1:]:
#     added = False
#     for i in range(len(subsequences)):
#         if height == subsequences[i][-1] - 1:
#             subsequences[i].append(height)
#             added = True
#             break
#     if not added:
#         subsequences.append([height])
# print(len(subsequences))
