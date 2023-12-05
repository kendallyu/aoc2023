import collections


with open("input.txt") as f:
    lines = f.read().splitlines()

possible = 0
for line in lines:
    counts = collections.defaultdict(int)
    line = line.split(": ")[1]
    sets = line.split("; ")
    for s in sets:
        colors = s.split(", ")
        for color in colors:
            n, c = color.split()
            counts[c] = max(counts[c], int(n))
    power = 1
    for x in counts.values():
        power *= x
    possible += power

print(possible)