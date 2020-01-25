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
    acc = n
    while prime * prime <= n:
        prime = primes[i]
        if n % prime == 0:
            totient_memo[n] = totient(prime) * totient(n // prime)
            return totient_memo[n]
        i += 1
    if (n > 1):
        acc = acc * (1 - (1 / (n)))
    totient_memo[n] = int(acc)
    primes.append(n)
    return int(acc)


def is_permutation(n, k):
    n = str(n)
    k = str(k)
    if len(n) != len(k):
        return False
    for char in n:
        if k.count(char) != n.count(char):
            return False
    return True


minTot = totient(2)
minN = 2
for n in range(3, 10**7):
    tot = totient(n)
    if is_permutation(n, tot):
        if minN/minTot > n/tot:
            minTot = tot
            minN = n
    print(minN, len(totient_memo), len(primes))
