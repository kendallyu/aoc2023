import sys

import bisect
import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

seeds = list(map(int, lines[0].split()[1:]))
intervals = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
print(intervals)

def overlaps(a, b, x, y):
    return a <= x < b or x <= a < y

line_number = 3
while line_number < len(lines):
    new_intervals = []
    while line_number < len(lines) and lines[line_number] != "":
        d, s, l = map(int, lines[line_number].split())
        for i in range(len(intervals)):
            x, y = intervals[i]
            if x == y:
                continue
            # I just realized this isn't correct if x < s < y < s + l since it doesn't
            # handle breaking up into 3 intervals rather than 1 or 2
            if overlaps(s, s+l, x, y):
                print(s, s+l, x, y)
                if s <= x:
                    if s + l >= y:
                        new_intervals.append((x + d - s, y + d - s))
                        intervals[i] = (0, 0)
                    else:
                        interval_length = s + l - x
                        new_intervals.append((x + d - s, x + interval_length - s))
                        intervals[i] = (x + interval_length, y)
                else:
                    interval_length = y - s
                    new_intervals.append((d, d + interval_length))
                    intervals[i] = (x, s)
        line_number += 1
    intervals = new_intervals + [(a, b) for (a, b) in intervals if a != b]
    line_number += 2

print(min(intervals))