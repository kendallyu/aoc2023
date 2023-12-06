import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

times = string_to_int_list(lines[0].split(": ")[1])
distance = string_to_int_list(lines[1].split(": ")[1])

product = 1
for t, d in zip(times, distance):
    x = 0
    for i in range(t):
        if i * (t - i) > d:
            x += 1
    product *= x

print(product)