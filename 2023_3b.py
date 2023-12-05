import collections

with open("input.txt") as f:
    lines = f.read().splitlines()

gears = collections.defaultdict(list)

def has_symbol(num, imin, imax, jmin, jmax):
    if num == "":
        return
    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if 0 < i < len(lines) and 0 < j < len(lines[i]) and lines[i][j] == '*':
                gears[(i,j)].append(num)

for i in range(len(lines)):
    num = ""
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            num += lines[i][j]
        if not lines[i][j].isdigit() or j == len(lines[i]) - 1:
            has_symbol(num, i-1, i+1, j-len(num)-1, j)
            num = ""

s = 0
for x in gears.values():
    if len(x) == 2:
        s += int(x[0]) * int(x[1])
print(s)