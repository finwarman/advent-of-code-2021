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

total = 0

for row in rows:
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

    # track valid possible candidate segment wirings (based off 1, 4, 7, 8)
    l = {
        'topleft': set(chars[4] - chars[1]),
        'topmiddle': set(chars[7] - chars[1]),
        'topright': set(chars[1]),
        'middle': set(chars[4] - chars[1]),
        'bottomleft': set(chars[8] - chars[7] - chars[4]),
        'bottommiddle': set(chars[8] - chars[7] - chars[4]),
        'bottomright': set(chars[1]),
    }
    segs = len(l.keys())

    # determine 0, 6, and possibly 9
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

    # filter new valid segment wirings
    singles = set()
    for i in range(segs):
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

    # collate results, find remaining allocations by filter duplicates
    results = {}
    found = set()
    for i in range(segs):
        for chars, digits in candidates.items():
            if len(digits) == 1:
                found.add(list(digits)[0])
                results[chars] = list(digits)[0]
            else:
                digits -= found

    ten = 1  # powers of ten
    t = 0
    for val in rhs[::-1]:
        x = results[frozenset(list(val))]
        t += ten * x
        ten = ten * 10
    # print(t)
    total += t

print(total)
# 974512
