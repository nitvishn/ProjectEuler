import addmath
import itertools

primes = addmath.primes_under(2000000)
primes_set = set(primes)

memo = {}
def factorise(n):
    return constructFactors(n, addmath.prime_factors(n))
    if n in memo:
        return memo[n]
    if n in primes_set:
        return set([1, n])
    factors = set([1, n])
    for factor in primes:
        if factor > n:
            break
        if n % factor == 0:
            # if not factor + n/factor in primes_set:
            #     return False
            factors.add(factor)
            factors = factors.union(factorise(n // factor))
            break
    if factors == {1, n}:
        primes.append(n)
        primes_set.add(n)
    memo[n] = factors
    return memo[n]

def constructFactors(n, prime_factors):
    factors = {1, }
    for k in range(1, len(prime_factors) + 1):
        for combo in itertools.combinations(prime_factors, k):
            acc = 1
            for m in combo:
                acc *= m
            factors.add(acc)
    return factors

def checkProperty(n):
    factors = constructFactors(n, addmath.prime_factors(n))
    for d in factors:
        if not (d + n/d in primes_set):
            return False
    return True

print(checkProperty(30))
# total = 0
# for n in range(1, 100000001):
#     if checkProperty(n):
#         print(n)
#         total += n
# print(total)
