import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

instructions = lines[0]
graph = {}
for line in lines[2:]:
    a, _, b, c = line.split()
    graph[a] = (b[1:-1], c[:-1])

loc = "AAA"
n = 0
while loc != "ZZZ":
    if instructions[n % len(instructions)] == 'L':
        loc = graph[loc][0]
    else:
        loc = graph[loc][1]
    n += 1

print(n)