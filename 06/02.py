#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = "06.txt"
# f = "demo.txt"
with open(f, 'r') as file:
    data = file.read()

numbers = [int(x) for x in data.strip().split(',')]

# ==== SOLUTION ====
total = 0

# days = 80
# days = 18  # demo
days = 256

ndict = {}

for n in range(-1, 9):
    ndict[n] = 0
for number in numbers:
    ndict[number] += 1

for d in range(days):
    for n in range(0, 9):
        x = ndict[n]
        ndict[n] = 0
        ndict[n-1] += x
    # -1 case
    x = ndict[-1]
    ndict[8] += x
    ndict[6] += x
    ndict[-1] = 0

print(sum(ndict.values()))


# Part 1 (80 days)
# Demo: 5934
# Answer: 363101

# Part 2 (256 days)
# Demo: 26984457539
# Answer: 1644286074024
