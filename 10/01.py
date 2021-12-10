#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '10.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

total = 0

closings = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

for row in rows:
    last_opened = [row[0]]
    for char in row[1:]:
        if char in closings:
            opened = last_opened.pop()
            if opened != closings[char]:
                total += points[char]
                break
        else:
            last_opened.append(char)

print(total)
# 364389
