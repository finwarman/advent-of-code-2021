#! /usr/bin/env python3

# ==== INPUT ====
data = ""
f = '09.txt'
# f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

grid = [[int(x) for x in list(row.strip())] for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

W = len(grid[0])
H = len(grid)

risk = 0

# finding basins = filling from low points to high points

lows = []

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
            lows.append((x, y))

basins = []
for low in lows:
    x, y = low
    candidates = [(x, y)]
    points = set()
    points.add((x, y))

    while len(candidates) > 0:
        x, y = candidates.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (y+dy >= 0 and y+dy < H) and (x+dx >= 0 and x+dx < W) \
                    and grid[y+dy][x+dx] < 9:
                p = (x+dx, y+dy)
                if p not in points:
                    candidates.append(p)
                points.add(p)
    basins.append(list(points))

basins.sort(key=len, reverse=True)
prod = 1
for x in basins[0:3]:
    prod *= len(x)
print(prod)

# 900900
