import addmath
primes=set(addmath.primes_under(9999))

def is_permutation(n1, n2):
    n1=str(n1)
    n2=str(n2)
    if(len(n1)!=len(n2)):
        return False
    for c in n1:
        if c not in n2:
            return False
    return True

def sequence(n):
    cursor=n
    for increment in range(3330, 3331):
        if(cursor+increment in primes and cursor+(2*increment) in primes):
            if(is_permutation(cursor, cursor+increment) and is_permutation(cursor, cursor+(2*increment))):
                return (cursor, cursor+increment, cursor+2*increment)
    return False
    
def concat(n):
    return str(n[0])+str(n[1])+str(n[2])

for prime in primes:
    if(sequence(prime)!=False):
        print(concat(sequence(prime)))