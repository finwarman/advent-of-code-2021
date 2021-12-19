#! /usr/bin/env python3
import copy
from itertools import permutations
import re
import math
from functools import reduce

# ==== INPUT ====
data = ""
f = '18.txt'
#f = 'demo.txt'
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

# print("\ntraversing\n")


# def postorder(root, depth, parent=None, side=None):
#     # return if the current node is empty
#     if root is None:
#         return False

#     if type(root) is int:
#         if root >= 10:
#             print("SPLIT: {}".format(root))
#             p = Pair(root//2, (root+1)//2, parent)
#             if side == 'right':
#                 parent.right = p
#             else:
#                 parent.left = p
#             return True
#         return

#     root.side = side

#     if depth == 4:
#         print("EXPLODE", side, root)
#         lhs = root.left
#         rhs = root.right

#         node = root
#         seen = {root}

#         while node.parent:
#             node = node.parent
#             if type(node.left) is int:
#                 node.left += lhs
#                 print(node.left, "left")
#                 break
#             if node.left and node.left not in seen:
#                 p = node
#                 node = node.left
#                 while type(node.right) is Pair:
#                     node = node.right
#                 print(node.right)
#                 node.right += lhs
#                 break
#             seen.add(node)

#         # if side == 'right':
#         #     parent.right = 0
#         # else:
#         #     parent.left = 0

#         node = root
#         seen = {root}

#         while node.parent:
#             node = node.parent
#             if type(node.right) is int:
#                 node.right += rhs
#                 print(node.right, "right")
#                 break
#             if node.right and node.right not in seen:
#                 p = node
#                 node = node.right
#                 while type(node.left) is Pair:
#                     node = node.left
#                 print(node.left)
#                 node.left += rhs
#                 break
#             seen.add(node)

#         if side == 'right':
#             parent.right = 0
#         else:
#             parent.left = 0

#         return True

#     # Traverse the left subtree
#     # if type(root.left) is not int:
#     x = postorder(root.left, depth+1, root, 'left')
#     if x is True:
#         return root

#     # Traverse the right subtree
#     # if type(root.right) is not int:
#     postorder(root.right, depth+1, root, 'right')

#     return root

def explode(pair, level, side=None):
    if type(pair) is int or pair is None:
        return
    pair.side = side

    if level == 4:
        parent = pair.parent

        lhs = pair.left
        rhs = pair.right
        # print("EXPLODE", pair)
        # print(pair.parent)

        node = pair
        seen = {pair}
        while node.parent:
            node = node.parent
            if (node.left or type(node.left) is int) and node.left not in seen:
                p = node
                node = node.left
                if type(node) is int:
                    p.left += lhs
                    break
                while node.right is not None and type(node.right) is not int:
                    node = node.right
                node.right += lhs
                break
            seen.add(node)

        node = pair
        seen = {pair}
        while node.parent:
            node = node.parent
            if (node.right or type(node.right) is int) and node.right not in seen:
                p = node
                node = node.right
                if type(node) is int:
                    p.right += rhs
                    break
                while node.left is not None and type(node.left) is not int:
                    node = node.left
                node.left += rhs
                break
            seen.add(node)

        if side == 'right':
            parent.right = 0
        else:
            parent.left = 0

    if type(pair.left) is not None:
        explode(pair.left, level + 1, 'left')

    if type(pair.right) is not None:
        explode(pair.right, level + 1, 'right')


def split(pair, parent, side=None):
    if pair is None:
        return False
    if type(pair) is int:
        if pair >= 10:
            # print("split", pair)
            p = Pair(pair//2, (pair+1)//2, parent)
            if side == 'right':
                parent.right = p
            else:
                parent.left = p
            return True
        else:
            return False
    if split(pair.left, pair, 'left'):
        return True
    if split(pair.right, pair, 'right'):
        return True
    return False


def reducerow(top_node):
    previous = ""
    while str(top_node) != previous:
        # for i in range(10):
        previous = str(top_node)
        explode(top_node, 0)
        split(top_node, None)
        # print()
    return top_node


def addrow(rowa, rowb):
    # rowa = reducerow(rowa)
    # rowb = reducerow(rowb)
    # return reducerow(Pair(rowa, rowb))
    p = Pair(rowa, rowb)
    rowa.parent = p
    rowb.parent = p
    return reducerow(p)


# row = "[[[[[9,8],1],2],3],4]"
# row = "[7,[6,[5,[4,[3,2]]]]]"
# row = "[[6,[5,[4,[3,2]]]],1]"
# row = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# row = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# row = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
# build tree

def magnitude(node, side=None):
    if node is None:
        return 0
    if type(node) is int:
        return node

    total = 0
    total += 3*magnitude(node.left)
    total += 2*magnitude(node.right)

    return total


# tree = reduce(addrow, rows)
# print(tree)
# print(magnitude(tree))
rows = [parserow(x) for x in rows]
print(max([magnitude(addrow(copy.deepcopy(x), copy.deepcopy(y)))
           for x, y in permutations(rows, 2)]))

# row = parserow(row)
# print(row)
# print()
# print(reducerow(row))

# result = rows[0]
# for row in rows[1:6]:
#     result = addrow(result, row)
#     print(result)

# print(rows[0])
# print(reducerow(parserow(row)))

# y = addrow(rows[0], rows[1])
# print(y)

# x = parserow(row)
# print(x)
# print(y)
# print(str(x) == str(y))
# print()

# x = reducerow(parserow(row))
# y = reducerow(addrow(rows[0], rows[1]))
# print(x)
# print(y)
# print(str(x) == str(y))
# print()

# print(rows[0])

# print(reducerow(parserow(row)))
