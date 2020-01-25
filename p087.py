import addmath

primes = addmath.primes_under(10000)

target = 50000000
expressed = set()

for a in primes:
    if a ** 2 >= target:
        break
    for b in primes:
        if a **2 + b ** 3 >= target:
            break
        for c in primes:
            if a ** 2 + b **3 + c**4 >= target:
                break
            expressed.add(a ** 2 + b **3 + c**4)
print(len(expressed))
