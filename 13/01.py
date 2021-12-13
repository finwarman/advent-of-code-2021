#! /usr/bin/env python3
import re
import math
import numpy as np

# ==== INPUT ====
data = ""
f = '13.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

rows = [row for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

dots = set()
folds = []

W = 0
H = 0

for row in rows:
    if row:
        if row[0] == 'f':
            lhs, rhs = row.split('=')
            folds.append((lhs[-1], int(rhs)))
        else:
            x, y = [int(x) for x in row.split(',')]
            dots.add((x, y))
            W = max(x, W)
            H = max(y, H)

grid = [[0 for _ in range(W+1)] for y in range(H+1)]
for dot in dots:
    x, y = dot
    grid[y][x] = 1
grid = np.array(grid)

for fold in folds[0:1]:
    axis, index = fold

    if axis == 'y':
        lhs = grid[0:index]
        rhs = np.flip(grid[index+1:], 0)
        grid = np.add(lhs, rhs)
    else:
        a = np.array_split(grid, [index], 1)
        lhs = a[0]
        rhs = np.flip(a[1][:, 1:], 1)  # remove first column

        grid = np.add(lhs, rhs)

total = 0
for row in grid:
    # print(row)
    for col in row:
        if col:
            total += 1
print(total)
