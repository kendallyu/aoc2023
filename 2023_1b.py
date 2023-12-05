import math


with open("input.txt") as f:
    lines = f.read().splitlines()

words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

val = 0
for line in lines:
    digits = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            digits.append(int(line[i]))
            i += 1
            continue
        for word, digit in words.items():
            if line[i:i+len(word)] == word:
                digits.append(digit)
                # i += len(word)  # oh I guess a letter can be part of multiple words
                i += 1
                break
        else:
            i += 1
    print(digits)
    val += 10*digits[0] + digits[-1]

print(val)