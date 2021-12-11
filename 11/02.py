#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '11.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

grid = [[int(x) for x in list(row.strip())] for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

W = len(grid[0])
H = len(grid)

N = W*H

for i in range(10000):
    local_flashes = 0
    flashed = set()
    for y in range(H):
        for x in range(W):
            grid[y][x] += 1
            if grid[y][x] > 9:
                grid[y][x] = 0
                flashed.add((x, y))
                local_flashes += 1

    for f in flashed.copy():
        x, y = f
        candidates = [(x, y)]

        while len(candidates) > 0:
            x, y = candidates.pop()
            for dx, dy in [(-1, 1), (-1, 0), (-1, -1), (1, 1),
                           (1, 0), (1, -1), (0, -1), (0, 1)]:
                if (y+dy >= 0 and y+dy < H) and (x+dx >= 0 and x+dx < W):
                    p = (x+dx, y+dy)
                    if p not in flashed:
                        grid[y+dy][x+dx] += 1
                        if grid[y+dy][x+dx] > 9:
                            grid[y+dy][x+dx] = 0
                            candidates.append(p)
                            flashed.add(p)
                            local_flashes += 1
    if local_flashes == N:
        print("Simultaneous Flash: {}".format(i+1))
        break
