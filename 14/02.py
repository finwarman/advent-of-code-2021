#! /usr/bin/env python3
import re
import math
from collections import defaultdict

# ==== INPUT ====
data = ""
f = '14.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

base = data.split('\n')[0]
rows = [row.strip() for row in data.split('\n')[2:-1]]

# ==== SOLUTION ====

ins = {}

for row in rows:
    lhs, rhs = row.split(" -> ")
    ins[lhs] = rhs

count = defaultdict(int)
pairs = defaultdict(int)

for l in set(base):
    count[l] = base.count(l)

for i in range(len(base) - 1):
    pairs[base[i:i+2]] += 1

for _ in range(40):
    p = pairs.copy()
    for pair in pairs:
        pair_count = pairs[pair]
        if pair_count:
            new = ins[pair]
            lhs, rhs = (pair[0]+new, new+pair[1])

            count[new] += pair_count
            p[pair] -= pair_count

            if lhs in ins:
                p[lhs] += pair_count
            if rhs in ins:
                p[rhs] += pair_count
    pairs = p

c = set(count.values())
print(max(c) - min(c))

# 3572761917024
