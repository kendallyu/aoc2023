import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

graph = collections.defaultdict(list)
S = None
for i, line in enumerate(lines):
    for j in range(len(line)):
        if line[j] == '|':
            nxt = [(i-1, j), (i+1, j)]
        elif line[j] == '-':
            nxt = [(i, j-1), (i, j+1)]
        elif line[j] == 'L':
            nxt = [(i-1, j), (i, j+1)]
        elif line[j] == 'J':
            nxt = [(i-1, j), (i, j-1)]
        elif line[j] == '7':
            nxt = [(i, j-1), (i+1, j)]
        elif line[j] == 'F':
            nxt = [(i, j+1), (i+1, j)]
        elif line[j] == '.':
            nxt = []
        elif line[j] == 'S':
            S = (i, j)
            nxt = []
        else:
            print(line[j])
            raise ValueError
        for s, t in nxt:
            if 0 <= s < len(lines) and 0 <= j < len(line):
                graph[(i, j)].append((s, t))

graph[S] = []
for x in graph:
    if S in graph[x]:
        graph[S].append(x)
    
visited = set()
nxt = [S]
while nxt:
    x = nxt.pop()
    if x not in visited:
        visited.add(x)
        nxt.extend(graph[x])

n = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (i, j) in visited:
            continue
        # check parity of number of intersections to the right
        down = 0
        up = 0
        for k in range(j+1, len(lines[i])):
            if (i, k) in visited:
                if (i+1, k) in graph[(i, k)]:
                    down += 1
                if (i-1, k) in graph[(i, k)]:
                    up += 1
        n += min(down, up) % 2

print(n)