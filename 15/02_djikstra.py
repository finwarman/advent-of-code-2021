#! /usr/bin/env python3
from os import path
import re
import math
import numpy as np
import collections
import networkx as nx
import queue
from collections import defaultdict

# ==== INPUT ====
data = ""
f = '15.txt'
# f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

grid = np.array([[int(x) for x in row.strip()]
                 for row in data.split('\n')[:-1]])

# ==== SOLUTION ====

# expand grid by 5 times
grid = np.block(
    [[((grid + i + j - 1) % 9) + 1 for j in range(5)]
     for i in range(5)]
)


def neighbours(x: int, y: int, m: int, n: int):
    return [
        (x, y) for x, y in
        [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        if 0 <= x < m and 0 <= y < n
    ]


H, W = grid.shape

# credit to https://github.com/StenAL/Advent-of-Code-2021/blob/main/src/day15.py


def dijkstra(memo, x_max, y_max, levels):
    q = queue.PriorityQueue()
    for k in levels:
        memo[k] = 1000000000
        q.put((99, k))
    memo[(0, 0)] = 0
    while not q.empty():
        pri, node = q.get()
        neighbors = neighbours(*node, x_max, y_max)
        for n in neighbors:
            d = memo[node] + levels[n]
            if d < memo[n]:
                memo[n] = d
                q.put((d, n))


points = defaultdict(int)
for y in range(H):
    for x in range(W):
        points[(x, y)] = grid[y][x]
del grid

memo = {}
dijkstra(memo, W, H, points)
ans = memo[(W - 1, H - 1)]
print(ans)

# 2976
