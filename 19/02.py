#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '19.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====
total = 0

for row in rows:
    total += 1

print(total)
