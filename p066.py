import math


def getPeriodDigit(n, period):
    return period[1][(n - 1) % len(period[1])]


def period(n):
    m = 0
    d = 1
    a0 = int(math.sqrt(n))
    a = a0
    counter = 0
    p = [a0, []]
    while a != 2 * a0:
        m = (d * a) - m
        d = (n - m**2) / d
        a = int((a0 + m) / d)
        counter += 1
        p[1].append(a)
    return p


numcache = {}
dencache = {}


def denominator(n, p):
    if n == 0:
        return 1
    elif n == 1:
        return p[1][0]
    if n in dencache:
        return dencache[n]
    dencache[n] = denominator(n - 1, p) * \
        getPeriodDigit(n, p) + denominator(n - 2, p)
    return dencache[n]


def numerator(n, p):
    if n == 0:
        return p[0]
    elif n == 1:
        return p[0] * p[1][0] + 1
    if n in numcache:
        return numcache[n]
    numcache[n] = numerator(n - 1, p) * \
        getPeriodDigit(n, p) + numerator(n - 2, p)
    return numcache[n]


def is_square(y):
    x = math.sqrt(y)
    if int(x) == x and int(x)**2 == y:
        return True
    return False


def minSolution(D):
    if is_square(D):
        return 0
    p = period(D)
    i = 0
    x = 0
    while(True):
        x = numerator(i, p)
        y = denominator(i, p)
        if x**2 - D*(y ** 2) == 1:
            return x
        i += 1


def isInt(x):
    return int(x) == x


N = 1000

best = 0
bestD = None
D = 0
while(D <= N):
    numcache = {}
    dencache = {}
    x = minSolution(D)
    if x >= best:
        bestD = D
        best = x
    D += 1

print(bestD)
