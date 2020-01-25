import itertools

allowed = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def unique(part):
    if part[0] != part[1] != part[2]:
        return True
    return False


def checkPossibility(combination):
    counts = {}
    for part in combination:
        for num in part:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > 2:
                return False
    one = []
    for k in counts:
        if k not in allowed:
            return False
        if counts[k] == 1:
            one.append(k)

    for i in range(len(combination)):
        part = combination[i]
        fail = True
        if part[1] != combination[i-1][2]:
            return False
        for c in part:
            if c in one:
                fail = False
                break
        if fail:
            return False
    if 10 not in one:
        return False
    if len(one) != 5:
        return False
    return one


def partitionfunc(n, k, l=1):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        return
    if k == 1:
        if n >= l:
            yield (n,)
        return
    for i in range(l, n + 1):
        for result in partitionfunc(n - i, k - 1, i):
            yield (i,) + result


def swap(i, j, L):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
    return L


def arrangeCombination(combo, ones):
    for i in range(len(combo)):
        part = combo[i]
        for j in range(len(part)):
            c = part[j]
            if c in ones:
                temp = combo[i][0]
                combo[i][j] = temp
                combo[i][0] = c
    lowest = min(ones)

    return combo

print(checkPossibility([[6, 5, 3], [10, 3, 1], [9, 1, 4], [8, 4, 2], [7, 2, 5]]))
for S in range(13, 19):
    parts = []
    for part in partitionfunc(S, 3):
        if unique(part):
            parts.append(list(part))

    possible = []
    for combination in itertools.permutations(parts, 5):
        count = checkPossibility(combination)
        if count:
            combination = arrangeCombination(list(combination), count)
            print(combination, count)
            possible.append(combination)
