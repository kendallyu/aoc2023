import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    steps = line.split(',')
    s = 0
    for step in steps:
        v = 0
        for c in step:
            v += ord(c)
            v *= 17
            v %= 256
        s += v
    print(s)