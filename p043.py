import addmath
import itertools
primes=[2, 3, 5, 7, 11, 13, 17]

def has_property(number):
    d1=1
    while(d1+2<10):
        d2=d1+1
        d3=d1+2
        if(int(str(number)[d1]+str(number)[d2]+str(number)[d3])%primes[d1-1]!=0):
            return False
        d1+=1
    return True

sumall=0
for perm in itertools.permutations([0,1,2,3,4,5,6,7,8,9],10):
    perm=addmath.number_from_digits(perm)
    if(has_property(perm)):
        print(perm)
        sumall+=int(perm)
print(sumall)
