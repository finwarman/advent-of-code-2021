#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '15.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

grid = [[int(x) for x in row.strip()] for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

# shortest path moving only right and down

minTotal = math.inf

W = len(grid[0])
H = len(grid)

min_dist = [[math.inf for x in range(W)] for y in range(H)]
t = 0
for x in range(W):
    t += grid[0][x]
    min_dist[0][x] = t

t = 0
for y in range(H):
    t += grid[y][0]
    min_dist[y][0] = t

for y in range(1, H):
    for x in range(1, W):
        v = grid[y][x]
        min_dist[y][x] = min(min_dist[y-1][x] + v, min_dist[y][x-1] + v)

for row in min_dist:
    print(row)

print()

print(min_dist[-1][-1] - min_dist[0][0])
