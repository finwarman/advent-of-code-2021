#! /usr/bin/env python3
from os import link, path
import re
import math
from collections import defaultdict

# ==== INPUT ====
data = ""
f = '12.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

links = defaultdict(set)

uppers = set()
lowers = set()

for row in rows:
    lhs, rhs = row.split("-")
    links[lhs].add(rhs)
    links[rhs].add(lhs)
    for x in lhs, rhs:
        if x.lower() == x:
            lowers.add(x)
        else:
            uppers.add(x)

links = dict(links)
paths = set()


def dfs(curr_node, visited, path):
    global paths
    visited[curr_node] += 1

    if curr_node == 'end':
        paths.add(','.join(path))
    elif (curr_node in lowers and visited[curr_node] > 1):
        return
    else:
        for node in links[curr_node]:
            dfs(node, visited.copy(), path + [curr_node])


dfs('start', defaultdict(int), [])

# for path in paths:
#     print(path)

print(len(paths))
