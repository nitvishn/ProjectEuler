import addmath

primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])

def isPrime(n):
    if n in primes:
        return True
    for i in primes:
        if n % i == 0:
            return False
    primes.add(n)
    return True

total = 0
for i in range(2, 2000000):
    print(i)
    if isPrime(i):
        total += i
print(total)
