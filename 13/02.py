#! /usr/bin/env python3
from matplotlib import pyplot as plt
import matplotlib.colors
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

for fold in folds:
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

grid = [np.where(x > 0.5, 1, 0) for x in grid]  # binary threshold

cmap = matplotlib.colors.ListedColormap(
    ['white', 'black'])  # binary colour map
plt.imshow(grid, interpolation='nearest', cmap=cmap)
plt.show()

# JZGUAPRB
