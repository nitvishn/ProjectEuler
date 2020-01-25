import itertools
import math


def isCube(n):
    if math.ceil(n**(1 / 3))**3 == n:
        return True
    return False


def isPermutation(n_int, k_int):
    n = str(n_int)
    k = str(k_int)
    if len(n) != len(k):
        return False
    for char in n:
        if n.count(char) != k.count(char):
            return False
    return True


def passesTest(n, S):
    count = 0
    for num in S:
        if isPermutation(num, n):
            count += 1
            if count > 5:
                break
    return count


cubes = set()
for i in range(2, 10000):
    cubes.add(i**3)

n = 345
numCubes = 0
count = 0
while(count != 5):
    n += 1
    count = passesTest(n**3, cubes)

print(n**3)
