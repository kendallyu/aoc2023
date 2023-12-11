import sys

import bisect
import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

rows = set(range(len(lines)))
cols = set(range(len(lines[0])))
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            rows.discard(i)
            cols.discard(j)

rows = sorted(rows)
cols = sorted(cols)

locs = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            col = j + bisect.bisect_left(cols, j)
            row = i + bisect.bisect_left(rows, i)
            locs.append((row, col))

d = 0
for x in range(len(locs)):
    for y in range(x + 1, len(locs)):
        q, r = locs[x]
        s, t = locs[y]
        d += abs(s - q) + abs(t - r)

print(d)