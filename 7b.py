import sys

import collections
import math

sys.setrecursionlimit(10000)

def string_to_int_list(l, delimiter=None):
    return list(map(int, l.split(delimiter)))

with open("input.txt") as f:
    lines = f.read().splitlines()

def type_(hand):
    counts = collections.defaultdict(int)
    for card in hand:
        if card != 'J':
            counts[card] += 1
    counts = sorted(counts.values())
    if counts:
        counts[-1] += hand.count('J')
    else:
        counts = [5]
    if counts == [2, 3]:
        return 3.5
    for i in range(5, 2, -1):
        if i in counts:
            return i
    if counts == [1, 2, 2]:
        return 2
    elif 2 in counts:
        return 1
    else:
        assert counts == [1, 1, 1, 1, 1]
    return 0

card_val = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10
}

def key(hand):
    return (type_(hand), list(map(lambda x: card_val[x] if x in card_val else int(x), hand)))

hands = []
for line in lines:
    hand, bid = line.split()
    hands.append((key(hand), hand, int(bid)))

hands.sort()
print(hands)

winnings = 0
for i, hand in enumerate(hands):
    winnings += (i + 1) * hand[-1]
print(winnings)