import math

def isPrime(n):
    if n<=1:
        return False

    if n==2:
        return True
    elif n%2==0:
        return False

    for i in range(2, math.ceil(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

primes=[]
for i in range(2, 2000000):
    if(isPrime(i)):
        primes.append(i)
print(sum(primes))