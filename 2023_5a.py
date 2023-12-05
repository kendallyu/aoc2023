import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

seeds = set(map(int, lines[0].split()[1:]))
print(seeds)

i = 3
while i < len(lines):
    new_seeds = set()
    while i < len(lines) and lines[i] != "":
        a, b, c = map(int, lines[i].split())
        to_remove = []
        for seed in seeds:
            if b <= seed < b + c:
                to_remove.append(seed)
                new_seeds.add(seed + a - b)
        for seed in to_remove:
            seeds.remove(seed)
        i += 1
    seeds = new_seeds | seeds
    print(seeds)
    i += 2

print(seeds)
print(min(seeds))