import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

n = 0
for line in lines:
    line = string_to_int_list(line)
    i = 0
    while set(line) != {0}:
        n += line[0] * (-1)**i
        line = [b - a for a, b in zip(line, line[1:])]
        i += 1

print(n)