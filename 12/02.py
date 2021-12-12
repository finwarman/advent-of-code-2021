#! /usr/bin/env python3
from os import link, path
import re
import math
from collections import defaultdict

# ==== INPUT ====
data = ""
f = '12.txt'
# f = 'demo.txt'
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


def dfs(curr_node, visited, path, small_allowed):
    global paths
    visited[curr_node] += 1

    if curr_node == 'end':
        paths.add(','.join(path))
        return
    elif (curr_node in lowers and visited[curr_node] > 1):
        if not small_allowed or curr_node == 'start':
            return
        small_allowed = False

    for node in links[curr_node]:
        dfs(node, visited.copy(), path + [curr_node], small_allowed)


dfs('start', defaultdict(int), [], True)

print(len(paths))
# 89592
