import addmath

LIMIT = 1000000
primes = addmath.primes_under(LIMIT)

def sopf(n):
    i = 0
    tot = 0
    prime = primes[i]
    while prime <= n:
        if n % prime == 0:
            tot += prime
        i += 1
        prime = primes[i]
    return tot

kappa_memo = {}
def kappa(n):
    if n == 0:
        return 0
    if n in kappa_memo:
        return kappa_memo[n]
    acc = sopf(n)
    for j in range(1, n):
        acc += sopf(j)*kappa(n-j)
    acc = acc//n
    kappa_memo[n] = acc
    return acc

print(kappa(997))
