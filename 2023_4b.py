import collections


def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

points = 0
counts = [1 for _ in range(len(lines))]

for i,line in enumerate(lines):
    card, numbers = line.split("|")
    card = set(map(int, card.split()[2:]))
    numbers = string_to_int_list(numbers)
    x = len([n for n in numbers if n in card])
    for j in range(i+1, i+x+1):
        counts[j] += counts[i]

print(sum(counts))