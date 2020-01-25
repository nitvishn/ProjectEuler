import math
from copy import copy
# p1 = (x1, y1)
# p2 = (x2, y2)


def distance_squared(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def triplet(x1, y1, x2, y2):
    lengths = [distance_squared(0, 0, x1, y1), distance_squared(
        0, 0, x2, y2), distance_squared(x1, y1, x2, y2)]
    if 0 in lengths:
        return False
    for hyp in lengths:
        remaining = copy(lengths)
        remaining.remove(hyp)
        total = 0
        for l in remaining:
            total += l
        if total == hyp:
            return True
    return False

past_coords = set()
upperbound = 50
counter = 0
for x1 in range(upperbound + 1):
    for y1 in range(upperbound + 1):
        for x2 in range(upperbound +1):
            for y2 in range(upperbound + 1):
                if (x2, y2) in past_coords:
                    continue
                if triplet(x1, y1, x2, y2):
                    counter += 1
                past_coords.add((x1, y1))
    print(x1)
print(counter)
