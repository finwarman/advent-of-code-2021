#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = '07.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

nums = sorted([int(x) for x in data.split(',')])
# ==== SOLUTION ====

# reduce search space by searching around the mean
avg = round(sum(nums)/len(nums))

minf = math.inf
for num in range(avg-1, avg+1):
    fuel = 0
    for x in nums:
        n = abs(x - num)
        fuel += (n * (n+1)) // 2
        if fuel > minf:
            break
    minf = min(fuel, minf)

print(minf)

# 101571302
