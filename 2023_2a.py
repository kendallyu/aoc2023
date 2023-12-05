import math


with open("input.txt") as f:
    lines = f.read().splitlines()

counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible = 0
for i, line in enumerate(lines):
    line = line.split(": ")[1]
    sets = line.split("; ")
    ok = True
    for s in sets:
        colors = s.split(", ")
        for color in colors:
            n, c = color.split()
            if counts[c] < int(n):
                ok = False
    if ok:
        possible += i + 1

print(possible)