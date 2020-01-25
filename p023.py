from addmath import *
from itertools import combinations
import time

def abundant(n):
    if(sum(factors(n))>n):
        return True
    return False
    
def produce_sums(abundantnums, upper):
    possible=[True]*(upper+1)
    for i in range(len(abundantnums)-1):
        for j in range(i, len(abundantnums)-1):
            if(abundantnums[i]+abundantnums[j] <= upper):
                possible[abundantnums[i] + abundantnums[j]]=False
            else:
                break
    return sum(convertNumbers(possible))
start=time.time()
upper=28123
abundantnums=[]
for i in range(upper):
    if(abundant(i)):
        abundantnums.append(i)
print(produce_sums(abundantnums, upper))
print(time.time()-start)

start=time.time()
def GetSumOfDivs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n%i == 0:
            upper = n/i
            total += upper
            if upper != i: total += i
        i += 1
    return total


def isabundant(n): return GetSumOfDivs(n) > n
lAbundants = [x for x in range(12, 28123) if isabundant(x) == True]
dAbundants = {x:x for x in lAbundants}

print(time.time()-start)