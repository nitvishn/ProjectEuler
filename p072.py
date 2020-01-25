import addmath


totient_memo = {}
print("Calculating primes...", end='')
primes = addmath.primes_under(1000000)
print("done.")


for prime in primes:
    totient_memo[prime] = prime - 1


def totient(n):
    if n in totient_memo:
        return totient_memo[n]
    i = 0
    prime = primes[i]
    while prime * prime < n:
        if n % prime == 0:
            k = n
            mult = 1
            while k % prime == 0:
                k = k // prime
                mult *= prime
            if mult == n:
                break
            totient_memo[n] = totient(mult) * totient(k)
            return totient_memo[n]
        i += 1
        prime = primes[i]

    acc = n
    for prime in set(addmath.prime_factors(n)):
        acc *= (1 - (1 / prime))

    totient_memo[n] = int(acc)
    primes.append(n)
    return int(acc)

# print("Totient:", totient(21))
N = 10**6
S = 0
for d in range(2, N + 1):
    tot = totient(d)
    print(d, tot)
    S += tot
print(S)
