import math
import addmath

def probability(b, r):
    return (b**2 - b), (b**2 + b*r - b + b*r + r**2 - r)

def findRNumerical(b):
    return (-(1-2*b)-math.sqrt(1 + 8*(b**2) - 8*b))/-2

def is_square(n):
    x = round(math.sqrt(n))
    if x**2 == n:
        return x
    return False

def exists(b):
    x = is_square(1 + 8*(b**2) - 8*b)
    if not x:
        return False
    x = -(1-2*b) - x
    if x % 2 != 0:
        return False
    return x//-2

def findRBinary(b):
    lower = 0
    upper = b
    r = (lower + upper)//2
    num, denom = probability(b, r)
    prev = None
    while lower < upper and prev != r:
        # print(r)
        if 2*num < denom:
            upper = r
        if 2*num > denom:
            lower = r
        if 2*num == denom:
            return r
        prev = r
        r = (lower + upper)//2
        num, denom = probability(b, r)
        # print(r, lower, upper, denom/num)
    return False

for b in range(1, 10**12):
    r = findRBinary(b)
    if r:
        print(b, r)
