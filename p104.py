import addmath

def pandigital(seq):
    # if len(str(seq)) != 9:
    #     return False
    return set(str(seq)) == set(str(123456789))

def property(n):
    n = str(n)
    if not pandigital(n[:9]):
        return False
    return pandigital(n[-9:])

i = 1
for n in addmath.fib():
    if pandigital(n % 10**9):
        print(i)
        if pandigital(str(n)[:9]):
            break
    i += 1
