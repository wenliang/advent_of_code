from collections import Counter
from itertools import accumulate

with open("day01_input.txt", "r") as f:
    bracks = [a for a in f.readline().strip()]

print("Q1:", Counter(bracks))
print(len(bracks))

# Q2
levels = [1 if a=="(" else -1 for a in bracks]
acc = list(accumulate(levels))
print(len(acc))
print([(i+1, v) for i,v in enumerate(acc) if v == -1])
