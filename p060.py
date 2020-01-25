import addmath
import itertools
import json
from copy import deepcopy


def testProperty(S):
    def concatenate(x, y):
        return int(str(x) + str(y))
    for x in S:
        for y in S:
            if x == y:
                continue
            conc = concatenate(x, y)
            if conc < 1000000:
                if conc not in primes:
                    return False
            elif not addmath.isPrime(concatenate(x, y)):
                return False
    return True


def amicable_brides(n, L):
    brides = []
    for item in L:
        if item[0] == n:
            brides.append(item[1])
        elif item[1] == n:
            brides.append(item[0])
    return brides


primes = set(addmath.primesFromFile('1mprimes.txt'))
print("loaded.")
#
testprimes = set(addmath.primesFromFile('10kprimes.txt'))

test = 7
filter = []
for prime in testprimes:
    if prime == test:
        continue
    if testProperty([test, prime]):
        filter.append(prime)

property_check = {}
for i in range(len(filter)):
    x = filter[i]
    for j in range(i, len(filter)):
        y = filter[j]
        if x == y:
            continue
        if testProperty([x, y]):
            property_check[x] = property_check.get(x, set())
            property_check[x].add(y)
    print("i:", i)

removed = [1]
while(removed != []):
    new_property_check = {}
    removed = []
    for key in property_check:
        if len(property_check[key]) < 4:
            removed.append(key)
            continue
        new_property_check[key] = property_check[key]
        for item in removed:
            if item in new_property_check[key]:
                new_property_check[key].remove(item)
    property_check = deepcopy(new_property_check)

property_check = new_property_check
possible = list(property_check.keys())

print(property_check)

for i in range(len(possible)):
    x = possible[i]
    for j in range(i, len(possible)):
        y = possible[j]
        intersect = list(property_check[x].intersection(property_check[y]))
        if (y in property_check[x]) and (len(intersect) >= 2):
            if(testProperty(intersect + [test, x, y])):
                print("Passed:", intersect + [test, x, y], sum(intersect + [test, x, y]))
            else:
                print("Failed:", intersect + [test, x, y], sum(intersect + [test, x, y]))
