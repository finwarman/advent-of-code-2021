#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('03.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

length = len(rows)
half = length // 2

bitG = ""
bitE = ""

for i in range(len(rows[0])):
    t = 0
    for row in rows:
        t += int(row[i])
    bitG = bitG + ("1" if t >= half else "0")
    bitE = bitE + ("0" if t >= half else "1")

print(bitG)
print(int(bitG, base=2))
print()
print(bitG)
print(int(bitG, base=2))
print()
print(int(bitG, base=2) * int(bitE, base=2))
