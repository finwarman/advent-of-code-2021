#! /usr/bin/env python3
import re
import math
from functools import reduce

# ==== INPUT ====
data = ""
f = '18.txt'
# f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====


class Pair:

    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.side = ''

    def __str__(self, indent=""):
        childString = ""

        if self.left is not None:
            if type(self.left) is int:
                childString += "\n{}├ {}".format(indent, self.left)
            else:
                childString += "\n{}├ {}".format(indent,
                                                 self.left.__str__(indent + "│ "))

        if self.right is not None:
            if type(self.right) is int:
                childString += "\n{}└ {}".format(indent, self.right)
            else:
                childString += "\n{}└ {}".format(indent,
                                                 self.right.__str__(indent + "  "))

        return "node{}: {}".format(" ("+self.side+")" if self.side else '', childString)


def parserow(row):
    i = 0
    count = 0
    top_node = Pair()
    stack = [top_node]
    while i < len(row):
        current_node = stack[-1]

        if row[i] == '[':
            node = Pair()
            count += 1
            if current_node.left is None:
                current_node.left = node
            else:
                current_node.right = node
            node.parent = current_node
            stack.append(node)

        if row[i].isdigit():
            if current_node.left is None:
                j = row.find(",", i)
                x = int(row[i:j])
                current_node.left = x
                i = j
            else:
                j = row.find("]", i)
                x = int(row[i:j])
                current_node.right = x
                i = j

        if row[i] == ']':
            stack.pop()

        i += 1

    top_node = top_node.left
    return top_node


def explode_row(pair, level, side=None):
    if type(pair) is int or pair is None:
        return
    pair.side = side

    if level == 4:
        parent = pair.parent

        lhs = pair.left
        rhs = pair.right

        visited = set()

        node = pair
        while node.parent:
            visited.add(node)
            node = node.parent
            if (node.left or type(node.left) is int) and node.left not in visited:
                p = node
                node = node.left
                if type(node) is int:
                    p.left += lhs
                    break
                while node.right is not None and type(node.right) is not int:
                    node = node.right
                node.right += lhs
                break

        visited = set()
        node = pair
        while node.parent:
            visited.add(node)
            node = node.parent
            if (node.right or type(node.right) is int) and node.right not in visited:
                p = node
                node = node.right
                if type(node) is int:
                    p.right += rhs
                    break
                while node.left is not None and type(node.left) is not int:
                    node = node.left
                node.left += rhs
                break

        if side == 'right':
            parent.right = 0
        else:
            parent.left = 0

    if type(pair.left) is not None:
        explode_row(pair.left, level + 1, 'left')

    if type(pair.right) is not None:
        explode_row(pair.right, level + 1, 'right')


def split_row(pair, parent, side=None):
    if pair is None:
        return False
    if type(pair) is int:
        if pair >= 10:
            p = Pair(pair//2, (pair+1)//2, parent)
            if side == 'right':
                parent.right = p
            else:
                parent.left = p
            return True
        else:
            return False
    else:
        modified = split_row(pair.left, pair, 'left')
        if not modified:
            modified = split_row(pair.right, pair, 'right')
        return modified


def reducerow(top_node):
    previous = ""
    while str(top_node) != previous:
        previous = str(top_node)
        explode_row(top_node, 0)
        split_row(top_node, None)
    return top_node


def addrow(rowa, rowb):
    p = Pair(rowa, rowb)
    rowa.parent = p
    rowb.parent = p
    return reducerow(p)


def magnitude(node, side=None):
    if node is None:
        return 0
    if type(node) is int:
        return node

    total = 0
    total += 3*magnitude(node.left)
    total += 2*magnitude(node.right)
    return total


rows = [parserow(x) for x in rows]

tree = reduce(addrow, rows)
print(tree)
print(magnitude(tree))
# 4417
