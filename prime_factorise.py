import addmath
import time
import pylab

global primes
primes=addmath.primesFromFile("2mprimes.txt")

def prime_factorise(n):
    """

    Recursive algorithm to prime factorise a number.

    First, find a prime factor for n. Add it to a list, L.

    :param n:
    :return list of primes whose product is n.:

    """
    L=[] #List of factors, factors need not be prime.

    for prime in primes:
        if n%prime==0:
            L.append(prime)
            if(n/prime != 1):
                L.extend(prime_factorise(n/prime))
                return L
            return L

def prime_factorise2(n):
    """

    A function that tells you to fuck yourself, because it's (apparently not) faster and took 1/10 the time to develop.

    :param n:
    :return L, a list of prime factors:
    """
    L=[]
    for prime in primes:
        while(n%prime==0):
            L.append(prime)
            n/=prime
        if(n==1):
            return L

startVal=2
maxVal=2000

firstData=[]
secondData=[]
for n in range(startVal, maxVal):
    start=time.time()
    prime_factorise(n)
    firstData.append((time.time()-start)*1000000)

for n in range(startVal, maxVal):
    start=time.time()
    prime_factorise2(n)
    secondData.append((time.time()-start)*1000000)

pylab.figure()
pylab.title("Iteration vs. Recursion")
pylab.plot(list(range(startVal, maxVal)), secondData, label="Iterative Algorithm")
pylab.plot(list(range(startVal, maxVal)), firstData, label="Recursive Algorithm")
pylab.xlabel("Number which is prime factorised")
pylab.ylabel("Time taken to prime factorise (in microseconds)")
print(firstData)
pylab.legend()
pylab.show()

