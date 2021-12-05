#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('02.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

depth = 0
pos = 0
aim = 0

for row in rows:
    cmd, val = row.split(" ")
    x = int(val)

    if cmd == "forward":
        pos += x
        depth += x * aim
    elif cmd == "down":
        aim += x
    elif cmd == "up":
        aim -= x

print(depth * pos)
