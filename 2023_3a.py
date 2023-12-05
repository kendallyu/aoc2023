with open("input.txt") as f:
    lines = f.read().splitlines()

s = 0

def has_symbol(imin, imax, jmin, jmax):
    print(imin, imax, jmin, jmax)
    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if 0 < i < len(lines) and 0 < j < len(lines[i]) and lines[i][j] != '.' and not lines[i][j].isdigit():
                return True
    return False

for i in range(len(lines)):
    num = ""
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            num += lines[i][j]
        if not lines[i][j].isdigit() or j == len(lines[i]) - 1:
            if not num == "" and has_symbol(i-1, i+1, j-len(num)-1, j):
                s += int(num)
                print(num)
            num = ""

print(s)