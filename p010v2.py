from math import *
import time

limit = int(input("Upperbound: "))
crosslimit = int(sqrt(limit))
if(crosslimit < 20):
    crosslimit = limit
sieve = [True] * limit
sieve[0] = False

for n in range(4, limit, 2):
    sieve[n - 1] = False

for n in range(3, limit, 2):
    if sieve[n - 1]:
        for m in range(n * n, limit, 2 * n):
            sieve[m - 1] = False

primes = []
for n in range(2, limit):
    if sieve[n - 1]:
        primes.append(n)

print(sum(primes))
