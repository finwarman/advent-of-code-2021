#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '17.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

xmin, xmax, ymin, ymax = [int(x) for x in re.findall(r'-?\d+', data)]

# ==== SOLUTION ====
x, y = 0, 0

print(xmin, xmax, ymin, ymax)

valid_initials = set()

for vx in range(-xmax, xmax + 1):
    for vy in range(ymin, -ymin + 1):
        dx, dy = vx, vy
        x, y = 0, 0

        while x < xmax+1 and y > ymin-1:
            x += dx
            y += dy

            dx = 0 if dx == 0 else dx - (dx // abs(dx))
            dy -= 1

            if x >= xmin and x <= xmax:
                if y <= ymax and y >= ymin:
                    valid_initials.add((vx, vy))
                    break

print(len(valid_initials))
# 1733
