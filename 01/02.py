#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('01.txt', 'r') as file:
    data = file.read()

rows = [int(row.strip()) for row in data.split('\n')[:-1]]  # trims empty row

# ==== SOLUTION ====

# 0-50 signal strength
total = -1
prev = -1
for i in range(len(rows)-2):
    window = rows[i:i+3]
    sw = sum(window)
    if sw > prev:
        total += 1
    prev = sw

print(total)
