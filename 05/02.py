#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = "05.txt"
#f = "demo.txt"
with open(f, 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

rows = [row.split(" -> ") for row in rows]
rows = [[[int(x) for x in col.split(",")] for col in row] for row in rows]

# ==== SOLUTION ====
max_x = max_y = 0

lines = []

for row in rows:
    for point in row:
        max_x = max(point[0]+1, max_x)
        max_y = max(point[1]+1, max_y)
    lines.append(row)

print("Grid Size:", max_x, max_y)

hits = [[0 for x in range(max_x)] for y in range(max_y)]

# get all integer points in line segment
for line in lines:
    (x1, y1), (x2, y2) = line[0], line[1]

    dx, dy = (x2 - x1), (y2 - y1)
    unit_dx = 0 if dx == 0 else dx // abs(dx)
    unit_dy = 0 if dy == 0 else dy // abs(dy)

    # same as above, but using copysign
    # unit_dx = int(math.copysign(min(abs(dx), 1), dx))
    # unit_dy = int(math.copysign(min(abs(dy), 1), dy))

    hi_x, lo_x, hi_y, lo_y = max(x1, x2), min(x1, x2), max(y1, y2), min(y1, y2)

    x, y = x1, y1
    while (x <= hi_x and x >= lo_x) and (y <= hi_y and y >= lo_y):
        hits[y][x] += 1

        x += unit_dx
        y += unit_dy

t = 0
for row in hits:
    for col in row:
        if col >= 2:
            t += 1
print(t)
# remember, run with pypy!

# ans:
# Grid Size: 989 990
# 20500
