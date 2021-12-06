#! /usr/bin/env python3
import re
import math
from timeit import default_timer as timer


# ==== INPUT ====
data = ""
f = "06.txt"
# f = "demo.txt"
with open(f, 'r') as file:
    data = file.read()

numbers = [int(x) for x in data.strip().split(',')]

# ==== SOLUTION ====

# days = 18
# days = 80
days = 256

start = timer()

for _ in range(1000):
    ndict = {k: 0 for k in range(-1, 9)}

    for number in numbers:
        ndict[number] += 1

    for d in range(days):
        for n in range(0, 9):
            x = ndict[n]
            ndict[n] = 0
            ndict[n-1] += x
        # -1 case: create children
        x = ndict[-1]
        ndict[8] += x
        ndict[6] += x
        ndict[-1] = 0

print(sum(ndict.values()))

end = timer()
print("Time:", end - start)  # Time in seconds

start = timer()

for _ in range(1000):

    narr = [0 for _ in range(0, 10)]
    for n in numbers:
        narr[n+1] += 1

    for d in range(days):
        for n in range(1, 10):
            x = narr[n]
            narr[n] = 0
            narr[n-1] += x
        # '-1' case: create children
        x = narr[0]
        narr[9] += x
        narr[7] += x
        narr[0] = 0

print(sum(narr))

end = timer()
print("Time:", end - start)  # Time in seconds

# Part 1 (80 days)
# Demo: 5934
# Answer: 363101

# Part 2 (256 days)
# Demo: 26984457539
# Answer: 1644286074024
