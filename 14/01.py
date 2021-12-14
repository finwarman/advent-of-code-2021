#! /usr/bin/env python3
import re
import math

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

n = 10
for j in range(n):
    new = base[0]
    for i in range(len(base) - 1):
        x, y = base[i:i+2]
        xy = x + y
        if xy in ins:
            new += ins[xy]
        new += y
    base = new

c = [base.count(l) for l in set(base)]
print(max(c) - min(c))
