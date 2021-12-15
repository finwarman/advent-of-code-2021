#! /usr/bin/env python3
from os import path
import re
import math
import numpy as np
import collections
import networkx as nx

# ==== INPUT ====
data = ""
f = '15.txt'
# f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

grid = [[int(x) for x in row.strip()] for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

# shortest path moving only right and down

minTotal = math.inf

W = len(grid[0])
H = len(grid)


grid = np.array(grid)

# built 5x larger grid
for n in range(4):
    p = [[x % 9 + 1 for x in row]
         for row in grid[n*H:(n+1)*H, 0:W]]
    grid = np.append(grid, p, 0)

last = grid.copy()
for n in range(4):
    p = [[x % 9 + 1 for x in row]
         for row in last]
    grid = np.append(grid, p, 1)
    last = p


def neighbours(x: int, y: int, m: int, n: int):
    return [
        (x, y) for x, y in
        [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        if 0 <= x <= m and 0 <= y <= n
    ]


H, W = grid.shape

g = nx.grid_2d_graph(H, W, create_using=nx.DiGraph)
for y in range(H):
    for x in range(W):
        for neighbour in neighbours(x, y, H, W):
            g.add_edge(neighbour, (x, y), weight=grid[x][y])


pathlen = nx.shortest_path_length(
    g, (0, 0), target=(H - 1, W - 1), weight="weight")
print(pathlen)

# 2976
