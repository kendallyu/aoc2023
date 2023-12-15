import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

def HASH(label):
    v = 0
    for c in label:
        v += ord(c)
        v *= 17
        v %= 256
    return v

for line in lines:
    steps = line.split(',')
    boxes = collections.defaultdict(dict)
    for i,step in enumerate(steps):
        if '=' in step:
            label, focal_length = step.split('=')
            if label in boxes[HASH(label)]:
                boxes[HASH(label)][label] = (boxes[HASH(label)][label][0], int(focal_length))
            else:
                boxes[HASH(label)][label] = (i, int(focal_length))
        else:
            label = step[:-1]
            try:
                boxes[HASH(label)].pop(label)
            except:
                pass
    focusing_power = 0
    for box_number, b in boxes.items():
        for slot_number, (_, focal_length) in enumerate(sorted(b.values())):
            focusing_power += (box_number + 1) * (slot_number + 1) * focal_length
    print(focusing_power)