import math


with open("input.txt") as f:
    lines = f.read().splitlines()

points = 0
for line in lines:
    card, numbers = line.split("|")
    card = set(map(int, card.split()[2:]))
    numbers = list(map(int, numbers.split()))
    x = len([n for n in numbers if n in card])
    if x > 0:
        points += 2**(x-1)

print(points)