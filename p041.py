import sys
sys.path.append('../libraries')
import addmath

def pandigital(number, n):
    number_set = addmath.get_digits(number)
    if(len(number_set)!=len(str(number)) or 0 in number_set):
        return False
    for i in range(1, n):
        if i not in number_set:
            return False
    return True

primes=addmath.primes_under(7654321)
for i in range(len(primes)-1, -1,-1):
    if(pandigital(primes[i], 7)):
        print(primes[i])
        break
