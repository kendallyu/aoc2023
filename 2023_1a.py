import math


with open("input.txt") as f:
    lines = f.read().splitlines()

val = 0
for line in lines:
    digits = [int(char) for char in line if char.isdigit()]
    val += 10*digits[0] + digits[-1]

print(val)