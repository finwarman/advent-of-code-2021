#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('03.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

w = len(rows[0])

considered = set(rows)
oxygen = None
for i in range(w):
    zero = 0
    one = 0
    for row in considered:
        if row[i] == '0':
            zero += 1
        else:
            one += 1

    starter = '1' if one >= zero else '0'
    for row in list(considered):
        if (row[i] != starter) and (row in considered):
            considered.remove(row)
    if len(considered) == 1:
        oxygen = considered.pop()
        break
print(oxygen)
print(int(oxygen, base=2))

print()

considered = set(rows)
co2 = None
for i in range(w):
    zero = 0
    one = 0
    for row in considered:
        if row[i] == '0':
            zero += 1
        else:
            one += 1

    starter = '1' if one >= zero else '0'
    for row in list(considered):
        if row[i] == starter and row in considered:
            considered.remove(row)

    if len(considered) == 1:
        co2 = considered.pop()
        break
print(co2)
print(int(co2, base=2))

print()
print
print(int(oxygen, base=2) * int(co2, base=2))
