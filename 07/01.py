#! /usr/bin/env python3
import re
import math
import statistics

# ==== INPUT ====
data = ""
f = '07.txt'
# f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

nums = sorted([int(x) for x in data.split(',')])
# ==== SOLUTION ====

# median solution
mid = nums[len(nums)//2]
fuel = sum([abs(x - mid) for x in nums])
print(fuel)

# bruteforce solution
# minf = nums[-1] * len(nums)
# for num in nums:
#     fuel = 0
#     for x in nums:
#         fuel += abs(x - num)
#     minf = min(fuel, minf)
# print(minf)
