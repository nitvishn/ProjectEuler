import itertools
from copy import copy


def satisfies_property(input_c1, input_c2):
    not_found = set([1, 4, 9, 16, 25, 36, 49, 64, 81])
    c1 = copy(input_c1)
    c2 = copy(input_c2)
    if 6 in c1:
        c1.add(9)
    elif 9 in c1:
        c1.add(6)
    if 6 in c2:
        c2.add(9)
    elif 9 in c2:
        c2.add(6)
    for a in c1:
        for b in c2:
            if 10*a + b in not_found:
                not_found.remove(10*a + b)
            if 10*b + a in not_found:
                not_found.remove(10*b + a)
    if len(not_found) == 0:
        return True
    return False


choiceset = set(range(0, 10))

arrangements = set()

counter = 0
for c1 in itertools.combinations(choiceset, 6):
    for c2 in itertools.combinations(choiceset, 6):
        c1, c2 = set(c1), set(c2)
        add_unit = frozenset([frozenset(c1), frozenset(c2)])
        if add_unit in arrangements:
            continue
        if satisfies_property(c1, c2):
            counter += 1
            arrangements.add(add_unit)
print(counter)
