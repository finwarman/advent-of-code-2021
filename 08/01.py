#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
f = '08.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====
total = 0

for row in rows:
    lhs, rhs = row.split(" | ")
    rhs = rhs.split(" ")

    # total += sum([1 for dig in rhs if len(dig) in [2, 4, 3, 7]])
    for dig in rhs:
        if len(dig) in [2, 4, 3, 7]:
            total += 1

print(total)


'''
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg


 e.g.
  1: c & f
  2: a & c & d & e & g
  ...
  7: a & c & f



Len Digits  |  Value
7               8
3               7
4               4
2               1
'''
