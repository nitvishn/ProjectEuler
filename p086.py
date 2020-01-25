import os
import math

def hcf(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


def is_int(n, epsilon=0):
    return 0 <= abs(int(n) - n) <= epsilon


def is_square(apositiveint):
    x = math.sqrt(apositiveint)
    if int(x)**2 == apositiveint:
        return int(x)
    return False
    # if apositiveint == 1:
    #     return 1
    # x = apositiveint // 2
    # seen = set([x])
    # while x * x != apositiveint:
    #     x = (x + (apositiveint // x)) // 2
    #     if x in seen:
    #         return False
    #     seen.add(x)
    # return x

def passes(a, b, c):
    return is_square(a**2 + (b + c)**2)
    # L = [a, b, c]
    # L.sort(reverse=True)
    # a, b, c = L[0], L[1], L[2]

    t1_numer = a**2 * b**2 + (b**2) * (b + c)**2
    t1_denom = (b + c)**2
    t1_divisor = hcf(t1_numer, t1_denom)
    t1_numer = t1_numer // t1_divisor
    t1_denom = t1_denom // t1_divisor

    t1_numer = is_square(t1_numer)
    t1_denom = is_square(t1_denom)

    if not (t1_numer and t1_denom):
        return False

    t2_numer = (a**2 * c**2) + (c**2) * (b + c)**2
    t2_denom = (b + c)**2
    t2_divisor = hcf(t2_numer, t2_denom)
    t2_numer = t2_numer // t2_divisor
    t2_denom = t2_denom // t2_divisor

    t2_numer = is_square(t2_numer)
    t2_denom = is_square(t2_denom)

    if not (t2_numer and t2_denom):
        return False

    numer = (t1_numer * t2_denom) + (t2_numer * t1_denom)
    denom = t1_denom * t2_denom

    if numer % denom == 0:
        return numer // denom
    return False


def number_solutions(M, prev=False):
    sols = 0
    if prev:
        a = M
        sols = prev
    else:
        a = 1
    while a <= M:
        b = 1
        while b <= a:
            c = 1
            while c <= b:
                if passes(a, b, c):
                    sols += 1
                c += 1
            b += 1
        a += 1
    return sols

# print(passes(6, 5, 3))
m = 1150
sols = 378129
while sols <= 1000000:
    m += 1
    print(m, sols)
    sols = number_solutions(m, sols)
print(m)
