import fractions

def getPeriodDigit(place):
    if place == 0:
        return 2
    if (place - 2) % 3 == 0:
        place = ((place - 2) / 3) + 1
        return int(place * 2)
    return 1


numcache = {}


def numerator(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    if n in numcache:
        return numcache[n]
    numcache[n] = numerator(n - 1) * getPeriodDigit(n) + numerator(n - 2)
    return numcache[n]


conv = 99
tot = 0
for digit in str(int(numerator(conv))):
    tot += int(digit)
print(tot)
