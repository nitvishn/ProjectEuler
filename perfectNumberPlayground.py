import addmath


def mersenne(k):
    return (2**k)-1

def perfectNumber(k):
    return ((2**k)-1)*(2**(k-1))

primes=set(addmath.primesFromFile("2mprimes.txt"))

for k in range(2, 1000):
    if(mersenne(k) in primes):
        print(perfectNumber(k), '   ', str(2**(k-1)), str((2**k)-1))