import math
from copy import deepcopy

LIMIT = 1500000


def pythagoreanTriplets(limits):
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            if a + b + c > limits:
                break

            k = 1

            while a*k + b*k + c*k <= limits:
                yield frozenset((a*k, b*k ,c*k))
                k += 1

        m = m + 1

triplets = set()
for triplet in pythagoreanTriplets(LIMIT):
    triplets.add(triplet)

sum_counts = {}
for triplet in triplets:
    sum_counts[sum(triplet)] = sum_counts.get(sum(triplet), 0) + 1

print(len([k for k,v in sum_counts.items() if v == 1]))
