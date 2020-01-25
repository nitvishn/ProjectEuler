import addmath

primes = addmath.primes_under(1000000)
check_primes=set(primes)
sumall=0
for i in range(len(primes)):
    prime=primes[i]
    sumall+=prime
    if(sumall>1000000):
        current=0
        while sumall not in check_primes:
            print("subtracting", primes[i-current], i-current,"from", sumall)
            sumall-=primes[i-current]
            current+=1
        print(sumall)
        break

