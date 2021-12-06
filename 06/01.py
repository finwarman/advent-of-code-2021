#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
f = "06.txt"
# f = "demo.txt"
with open(f, 'r') as file:
    data = file.read()

numbers = [int(x) for x in data.strip().split(',')]

# ==== SOLUTION ====
total = 0

days = 80
# days = 18  # demo
# days = 256

# print(numbers)
for d in range(days):
    # print("Day", d+1)

    new_numbers = []
    for i in range(len(numbers)):
        n = numbers[i]
        n = n - 1
        if n == -1:
            numbers[i] = 6
            new_numbers.append(8)
        else:
            numbers[i] = n
    numbers = numbers + new_numbers

    # print(numbers)

print(len(numbers))
