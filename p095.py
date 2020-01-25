import addmath
import pylab as plt
import networkx as nx
from copy import copy

next_memo = {}
def next(n):
    if n in next_memo:
        return next_memo[n]
    fact = addmath.factors(n) - {n, }
    next_memo[n] = sum(fact)
    return next_memo[n]

def loadMemo():
    file = open('p095_nexts.txt', 'r')
    for line in file:
        line = line.split(',')
        next_memo[int(line[0])] = int(line[1])
    global reverse
    reverse = set()
    for key in next_memo:
        reverse.add(next_memo[key])
    print("Finished loading.")

chain_memo = {}
def chain(n):
    if n in chain_memo:
        return chain_memo[n]
    if n in primes:
        return 0
    if not (n in reverse):
        return 0
    k = next_memo[n]
    encountered = []
    length = 1
    while k != n:
        print(k)
        if k < n:
            return 0
        if k in primes or k >= limit:
            length = 0
            break
        if k in encountered:
            ind = encountered.index(k)
            encountered = encountered[ind:]
            for item in encountered:
                chain_memo[item] = len(encountered)
            return 0
        encountered.append(k)
        length += 1
        k = next(k)
    encountered.append(n)
    for enc in encountered:
        chain_memo[enc] = length
    return length


limit = 1000000
primes = addmath.primes_under(limit)

loadMemo()

chain(14316)
print("Done.")
chain(next(14316))
#
# bestVal = 220
# bestLen = 2
# for i in range(1, limit):
#     k = chain(i)
#     print(i, bestVal, bestLen)
#     if k > bestLen:
#         bestVal = i
#         bestLen = k
# print(bestVal)
