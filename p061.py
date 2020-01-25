import itertools

def num_digits(number):
    return len(str(number))


def figurateNumbers(order):
    if order == 3:
        def formula(x): return x * (x + 1) * (1 / 2)
    elif order == 4:
        def formula(x): return x**2
    elif order == 5:
        def formula(x): return x * (3 * x - 1) * (1 / 2)
    elif order == 6:
        def formula(x): return x * (2 * x - 1)
    elif order == 7:
        def formula(x): return x * (5 * x - 3) * (1 / 2)
    elif order == 8:
        def formula(x): return x * (3 * x - 2)
    else:
        raise ValueError

    nums = []
    n = 0
    i = 1
    while(True):
        n = int(formula(i))
        digits = num_digits(n)
        if digits == 4:
            nums.append(str(n))
        elif digits > 4:
            break
        i += 1
    return nums


def findMatches(L, S):
    matches = []
    for x in L:
        for y in S:
            if str(x)[-2:] == str(y)[:2]:
                matches.append(str(x) + ',' + str(y))
    return matches


def getSolution(permutation):
    firstPairs = findMatches(
        figurates[permutation[0]], figurates[permutation[1]])
    secondPairs = findMatches(
        figurates[permutation[2]], figurates[permutation[3]])
    thirdPairs = findMatches(
        figurates[permutation[4]], figurates[permutation[5]])

    firstBits = findMatches(firstPairs, secondPairs)

    for item in firstBits:
        for item2 in thirdPairs:
            if item[-2:] == item2[:2] and item2[-2:] == item[:2]:
                return item +','+ item2


figurates = []
for order in range(3, 9):
    figurates.append(figurateNumbers(order))

plain = [0, 1, 2, 3, 4, 5]
for perm in itertools.permutations(plain):
    sol = getSolution(perm)
    if sol:
        sol = sol.split(',')
        sum = 0
        for num in sol:
            sum += int(num)
        print(sum)
        break
