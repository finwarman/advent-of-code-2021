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

closings = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

incomplete = []
for row in rows:
    corrupted = False
    last_opened = [row[0]]
    for char in row[1:]:
        if char in closings:
            opened = last_opened.pop()
            if opened != closings[char]:
                corrupted = True
                break
        else:
            last_opened.append(char)
    if not corrupted:
        incomplete.append(row)

scores = []
for row in incomplete:
    score = 0
    last_opened = [row[0]]
    for char in row[1:]:
        if char in closings:
            opened = last_opened.pop()
        else:
            last_opened.append(char)
    for x in last_opened[::-1]:
        score *= 5
        score += points[x]
    scores.append(score)

print(sorted(scores)[len(scores)//2])
