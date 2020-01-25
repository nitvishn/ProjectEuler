import addmath

def quadratic(a, b, n):
    return (n**2) + (a*n) + b

primes=addmath.primes_under(87400)

def isPrime(n):
    i=0
    while(primes[i]<=n):
        if(primes[i]==n):
            return True
        i+=1
    return False

print("produced primes")
aMax=bMax=nMax=0
for a in range(-1000, 0):
    for b in range(-1000, 1000):
        n=0
        while(isPrime(abs(quadratic(a, b, n)))):
            n+=1
        if(n>nMax):
            print("n2+"+str(a)+"n+"+str(b))
            nMax=n
            bMax=b
            aMax=a
            
print(aMax*bMax)