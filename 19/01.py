#! /usr/bin/env python3
import re
import math
import numpy as np

# ==== INPUT ====
data = ""
f = '19.txt'
f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

scanners = []
data = data.strip().split('\n\n')
for s in data:
    rows = s.split('\n')
    beacons = []
    for i in rows[1:]:
        x, y = i.split(',')
        beacons.append((int(x), int(y)))
    scanners.append(beacons)

# ==== SOLUTION ====

grids = []

abs_max_x = 0
abs_max_y = 0

for scanner in scanners:
    minx, miny = 0, 0
    for pos in scanner:
        x, y = pos
        minx = min(x, minx)
        miny = min(y, miny)

    maxx, maxy = 0, 0

    positions = set()
    for i in range(len(scanner)):
        x, y = scanner[i]

        nx = x-minx
        ny = y-miny

        n = (nx, ny)

        scanner[i] = n
        positions.add(n)

        maxx = max(maxx, nx)
        maxy = max(maxy, ny)

    abs_max_x = max(maxx, abs_max_x)
    abs_max_y = max(maxy, abs_max_y)

    ls = []
    for y in range(0, maxy+2):
        t = []
        for x in range(0, maxx+2):
            if (x, y) in positions:
                t.append(1)
            else:
                t.append(0)
        ls.append(t)

    # TODO: what is scanner pos
    #e.g. grid[y][x] = 2
    ls[-1 * miny][-1 * minx] = -1

    # grid of 1s for all beacons
    grids.append(np.array(ls))

template = np.zeros((abs_max_y+2, abs_max_x+2), dtype=np.int32)
H, W = template.shape

for i in range(len(grids)):
    grid = grids[i]

    t = template.copy()
    x, y = 0, 0
    t[x:x+grid.shape[0], y:y+grid.shape[1]] = grid
    grids[i] = t

# g1, g2 = (grids[0], grids[1])
# for grid in [g1, g2]:
#     print()
#     for row in grid:
#         print(row)
# print()

# x = g1 & g2
# print(x)


g1, g2 = grids[0], grids[1]

for y in range(H):
    g = g2.copy()
    for x in range(W):
        gx = np.roll(g, x, axis=1)
        print(gx)
        print(gx & g)
        # print(y, x)
        # print(g1 & gx)
