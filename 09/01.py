#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '09.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

grid = [[int(x) for x in list(row.strip())] for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

W = len(grid[0])
H = len(grid)

risk = 0

for y in range(H):
    for x in range(W):
        h = grid[y][x]

        low = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (y+dy >= 0 and y+dy < H) and (x+dx >= 0 and x+dx < W) \
                    and grid[y+dy][x+dx] <= h:
                low = False
                break

        if low:
            risk += 1 + h

print(risk)
