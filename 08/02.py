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
digits = {}

knownlengths = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}  # length -> digit

# potentials:
# len   |  candidates
#  7    |    8     DONE
#  6    |    0, 6, 9
#  5    |    2, 5, 3
#  4    |    4     DONE
#  3    |    7     DONE
#  2    |    1     DONE

# done:  0, 1, 2, _, 4, 5, _, 7, 8, 9

total = 0

for row in rows:
    complete = set()

    chars = {}
    candidates = {}

    lhs, rhs = row.split(" | ")
    lhs = lhs.split(" ")
    rhs = rhs.split(" ")

    for dig in lhs:
        n = len(dig)
        digset = set(list(dig))
        candidates[frozenset(digset)] = set()

        if n in knownlengths:
            candidates[frozenset(digset)] = set([knownlengths[n]])

        elif n == 6:
            candidates[frozenset(digset)] = set([0, 6, 9])

        elif n == 5:
            candidates[frozenset(digset)] = set([2, 5, 3])

    for key, s in candidates.items():
        if len(s) == 1:
            chars[list(s)[0]] = key

        # 1, 4, 7, 8
    topmiddle = chars[7] - chars[1]
    topleft = chars[4] - chars[1]  # candidates
    topright = chars[1]
    middle = chars[4] - chars[1]
    bottomleft = chars[8] - chars[7] - chars[4]
    bottommiddle = chars[8] - chars[7] - chars[4]
    bottomright = chars[1]

    l = {
        'topleft': set(topleft),
        'topmiddle': set(topmiddle),
        'topright': set(topright),
        'middle': set(middle),
        'bottomleft': set(bottomleft),
        'bottommiddle': set(bottommiddle),
        'bottomright': set(bottomright),
    }

    for key, s in candidates.items():
        if len(key) == 6:
            # topright, or middle
            (diff,) = set(chars[8]).difference(set(key))
            if diff in l['middle'] and diff not in l['middle'] and diff not in l['bottomleft']:
                l['middle'] = set(diff)
                candidates[key] = set([0])
                chars[0] = key
            elif diff in l['topright'] and diff not in l['middle'] and diff not in l['bottomleft']:
                l['topright'] = set(diff)
                candidates[key] = set([6])
                chars[6] = key
            elif diff in l['bottomleft']:
                candidates[key] = set([9])
                chars[9] = key

    singles = set()
    for i in range(7):
        for v in l.values():
            if len(v) == 1:
                singles.add(list(v)[0])

    for key in l.keys():
        if len(l[key]) > 1:
            l[key] -= singles

    # determine 2, 3, 5s

    for key, s in candidates.items():
        if len(key) == 5:
            if list(l['topright'])[0] not in key:
                candidates[key] = set([5])
                chars[5] = key
            elif list(l['bottomright'])[0] not in key:
                candidates[key] = set([2])
                chars[2] = key
            else:
                candidates[key] = set([3])
                chars[3] = key

    results = {}
    found = set()
    for i in range(7):
        for chars, digits in candidates.items():
            if len(digits) == 1:
                found.add(list(digits)[0])
                results[chars] = list(digits)[0]
            else:
                digits -= found

    ten = 1
    t = 0
    for val in rhs[::-1]:
        x = results[frozenset(list(val))]
        t += ten * x
        ten = ten * 10
    # print(t)
    total += t

print(total)
'''
acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3

Len Digits  |  Value
7               8
3               7
4               4
2               1

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc


'''
