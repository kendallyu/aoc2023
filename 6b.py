import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

t = int(''.join(lines[0].split()[1:]))
d = int(''.join(lines[1].split()[1:]))

min = math.ceil((t - math.sqrt(t**2-4*d)) / 2)
max = math.floor((math.sqrt(t**2-4*d)+t) / 2)
print(max - min + 1)