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

abs_max_y = 0
ideal_vels = (0, 0)
for vx in range(-xmax, xmax + 1):
    for vy in range(ymin, -ymin + 1):
        dx, dy = vx, vy
        x, y = 0, 0
        max_y = 0

        while x < xmax+1 and y > ymin-1:
            x += dx
            y += dy

            dx = 0 if dx == 0 else dx - (dx // abs(dx))
            dy -= 1

            max_y = max(y, max_y)

            if x >= xmin and x <= xmax:
                if y <= ymax and y >= ymin:
                    if max_y > abs_max_y:
                        abs_max_y = max_y
                        ideal_vels = (vx, vy)
                    break

print(abs_max_y)
print(ideal_vels)

# 17766
# (10, 188)
